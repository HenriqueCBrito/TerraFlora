from datetime import timedelta
from django.utils.timezone import now
import requests
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from apps.crops.models import Culturas
from .models import Event, CropSuggestion, Storage
from apps.farm.models import Farm
from django.contrib import messages


def calendar_view(request):
    """Renders the calendar page."""
    return render(request, 'management/calendar.html')

@login_required
def fetch_weather(request):
    """Fetches the current weather and forecast for a user-specified location using WeatherAPI."""
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')

    if latitude and longitude:
        location = f"{latitude},{longitude}"
    else:
        location = 'Carpina, PE'

    url = f"http://api.weatherapi.com/v1/forecast.json?key={settings.WEATHER_API_KEY}&q={location}&lang=pt&days=1&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_summary = {
            "location": {
                "name": weather_data['location']['name'],
                "region": weather_data['location']['region']
            },
            "current": {
                "temp_c": weather_data['current']['temp_c'],
                "condition": weather_data['current']['condition']['text'],
                "wind_kph": weather_data['current']['wind_kph'],
                "humidity": weather_data['current']['humidity'],
            },
        }
        return JsonResponse(weather_summary)

    return JsonResponse({"error": "Could not retrieve weather data"}, status=response.status_code)

@login_required
@require_POST
def add_event(request):
    crop_id = request.POST.get('crop_id')
    title = request.POST.get('title')
    task_type = request.POST.get('task_type')
    description = request.POST.get('description', '')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    priority = request.POST.get('priority', 'Medium')

    crop = get_object_or_404(Culturas, id=crop_id)

    weather_summary = fetch_weather(request)  # Fetch weather data
    Event.objects.create(
        crop=crop,
        user=request.user,
        title=title,
        task_type=task_type,
        description=description,
        start_date=start_date,
        end_date=end_date,
        priority=priority,
        weather_summary=weather_summary.get('current', {}).get('condition', 'Sem dados meteorológicos')
    )
    return JsonResponse({'status': 'success'})



@login_required
@require_POST
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.title = request.POST.get('title')
    event.task_type = request.POST.get('task_type')
    event.description = request.POST.get('description', '')
    event.start_date = request.POST.get('start_date')
    event.end_date = request.POST.get('end_date')
    event.priority = request.POST.get('priority', 'Medium')
    event.completed = request.POST.get('completed') == 'true'

    event.save()
    return JsonResponse({'status': 'success'})

@login_required
@require_POST
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return JsonResponse({'status': 'success'})

@login_required
def daily_checklist(request):
    today = now().date()

    # Get all unfinished events in the past
    overdue_events = Event.objects.filter(
        user=request.user,
        start_date__lt=today,
        completed=False
    )

    # Move overdue events to today
    for event in overdue_events:
        event.start_date = today
        event.end_date += timedelta(days=(today - event.start_date.date()).days)
        event.save()

    # Fetch today's events
    todays_events = Event.objects.filter(
        user=request.user,
        start_date__date=today,
        completed=False
    )

    if request.method == 'POST':
        completed_events = request.POST.getlist('completed_events')

        # Mark events as completed
        for event_id in completed_events:
            event = Event.objects.filter(id=event_id, user=request.user).first()
            if event:
                event.completed = True
                event.save()

        messages.success(request, 'Checklist atualizado com sucesso!')
        return redirect('daily_checklist')

    return render(request, 'management/daily_checklist.html', {'events': todays_events})

@login_required
def shopping_list(request):
    if request.method == 'POST':
        budget = float(request.POST.get('budget'))
        farm_id = request.POST.get('farm_id')
        farm = Farm.objects.get(id=farm_id)

        # Convert farm size to m²
        farm_size_m2 = farm.size
        if farm.size_unit == 'ac':
            farm_size_m2 *= 4046.86
        elif farm.size_unit == 'ha':
            farm_size_m2 *= 10000

        shopping_list = []
        total_cost = 0
        for suggestion in CropSuggestion.objects.all():
            if suggestion.recommended_area > 0:
                quantity = farm_size_m2 / suggestion.recommended_area
            else:
                quantity = 1  # Default quantity for items without area recommendation

            cost = suggestion.average_cost * quantity
            if total_cost + cost <= budget:
                shopping_list.append({
                    'name': suggestion.name,
                    'category': suggestion.category,
                    'quantity': round(quantity, 2),
                    'unit': suggestion.unit,
                    'cost': round(cost, 2),
                })
                total_cost += cost

        return render(request, 'management/shopping_list.html', {
            'shopping_list': shopping_list,
            'total_cost': round(total_cost, 2),
            'budget': budget,
        })

    farms = request.user.farms.all()
    return render(request, 'management/shopping_form.html', {'farms': farms})

@login_required
def add_storage(request):
    cultures = Culturas.objects.filter(user=request.user)

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        culture_id = request.POST.get('culture')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        average_cost = request.POST.get('average_cost')
        recommended_area = request.POST.get('recommended_area')

        culture = None
        if culture_id:
            culture = get_object_or_404(Culturas, id=culture_id, user=request.user)

        # Validação básica
        if not all([product_name, category, quantity, unit, average_cost]):
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'management/add_storage.html', {'cultures': cultures})

        # Criar o armazenamento
        storage = Storage(
            user=request.user,
            culture=culture,
            product_name=product_name,
            category=category,
            quantity=float(quantity),
            unit=unit,
            average_cost=float(average_cost),
            recommended_area=float(recommended_area) if recommended_area else None,
        )
        storage.save()

        messages.success(request, 'Produto adicionado ao armazenamento com sucesso!')
        return redirect('list_storage')

    return render(request, 'management/add_storage.html', {'cultures': cultures})

@login_required
def update_storage(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id, user=request.user)
    cultures = Culturas.objects.filter(user=request.user)

    if request.method == 'POST':
        storage.product_name = request.POST.get('product_name')
        storage.category = request.POST.get('category')
        culture_id = request.POST.get('culture')
        storage.quantity = request.POST.get('quantity')
        storage.unit = request.POST.get('unit')
        storage.average_cost = request.POST.get('average_cost')
        storage.recommended_area = request.POST.get('recommended_area')

        # Update the associated culture, if any
        storage.culture = None
        if culture_id:
            storage.culture = get_object_or_404(Culturas, id=culture_id, user=request.user)

        # Basic validation
        if not all([storage.product_name, storage.category, storage.quantity, storage.unit, storage.average_cost]):
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'management/update_storage.html', {'storage': storage, 'cultures': cultures})

        storage.save()
        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('list_storage')

    return render(request, 'management/update_storage.html', {'storage': storage, 'cultures': cultures})

@login_required
def delete_storage(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id, user=request.user)

    if request.method == 'POST':
        storage.delete()
        messages.success(request, 'Produto removido do armazenamento com sucesso!')
        return redirect('list_storage')

    return render(request, 'management/confirm_delete_storage.html', {'storage': storage})

@login_required
def list_storage(request):
    storages = Storage.objects.filter(user=request.user)

    if not storages.exists():
        messages.info(request, 'Nenhum produto encontrado no seu armazenamento.')

    return render(request, 'management/list_storage.html', {'storages': storages})
