from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Culturas
import json

# View to register a new crop
@login_required
def register_crop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        crop_type = request.POST.get('crop_type')
        planting_season = request.POST.get('planting_season')
        harvest_season = request.POST.get('harvest_season')
        growing_conditions = request.POST.get('growing_conditions')
        compatible_plants = request.POST.get('compatible_plants')
        common_pests = request.POST.get('common_pests')
        watering_needs = request.POST.get('watering_needs')
        sun_exposure = request.POST.get('sun_exposure')
        notes = request.POST.get('notes', '')

        # Basic validation for required fields
        if not all([name, crop_type, planting_season, harvest_season, growing_conditions, watering_needs, sun_exposure]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'register_crop.html')

        # Create and save the new crop
        crop = Culturas(
            name=name,
            crop_type=crop_type,
            planting_season=planting_season,
            harvest_season=harvest_season,
            growing_conditions=growing_conditions,
            compatible_plants=compatible_plants,
            common_pests=common_pests,
            watering_needs=watering_needs,
            sun_exposure=sun_exposure,
            notes=notes,
            user=request.user  # Link the crop to the current user
        )
        crop.save()

        messages.success(request, 'Crop registered successfully!')
        return redirect('crop_detail', crop_id=crop.id)  # Redirect to the crop detail view

    else:
        # Display the form if the request method is GET
        return render(request, 'register_crop.html')


# View to display details of a specific crop
@login_required
def crop_detail(request, crop_id):
    crop = get_object_or_404(Culturas, id=crop_id)

    return render(request, 'crop_detail.html', {'crop': crop})


# View to list all crops for the logged-in user
@login_required
def crop_list(request):
    crops = Culturas.objects.filter(user=request.user)  # Fetch crops directly linked to the user

    if not crops.exists():
        messages.info(request, 'No crops found for your account.')

    return render(request, 'crop_list.html', {'crops': crops})

@login_required
def edit_crop(request, crop_id):
    crop = get_object_or_404(Culturas, id=crop_id, user=request.user)  # Ensure the crop belongs to the logged-in user

    if request.method == 'POST':
        crop.name = request.POST.get('name')
        crop.crop_type = request.POST.get('crop_type')
        crop.planting_season = request.POST.get('planting_season')
        crop.harvest_season = request.POST.get('harvest_season')
        crop.growing_conditions = request.POST.get('growing_conditions')
        crop.compatible_plants = request.POST.get('compatible_plants')
        crop.common_pests = request.POST.get('common_pests')
        crop.watering_needs = request.POST.get('watering_needs')
        crop.sun_exposure = request.POST.get('sun_exposure')
        crop.notes = request.POST.get('notes', '')

        # Basic validation for required fields
        if not all([crop.name, crop.crop_type, crop.planting_season, crop.harvest_season, crop.growing_conditions, crop.watering_needs, crop.sun_exposure]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'edit_crop.html', {'crop': crop})

        # Save updated crop
        crop.save()
        messages.success(request, 'Crop updated successfully!')
        return redirect('crop_detail', crop_id=crop.id)  # Redirect to the crop detail view

    return render(request, 'edit_crop.html', {'crop': crop})

@login_required
def delete_crop(request, crop_id):
    crop = get_object_or_404(Culturas, id=crop_id, user=request.user)  # Ensure the crop belongs to the logged-in user

    if request.method == 'POST':
        crop.delete()
        messages.success(request, 'Crop deleted successfully!')
        return redirect('crop_list')  # Redirect to the crop list view

    return render(request, 'confirm_delete.html', {'crop': crop})

@login_required
def planting_calculator(request, crop_id):
    crop = get_object_or_404(Culturas, id=crop_id, user=request.user)

    if request.method == 'POST':
        try:
            # Recebe os dados do corpo da requisição
            data = json.loads(request.body)
            desired_harvest = float(data.get('desired_harvest', 0))

            if desired_harvest <= 0:
                return JsonResponse({"error": "Por favor, insira um valor válido para a colheita desejada."}, status=400)

            # Realiza os cálculos
            adjusted_harvest = desired_harvest / ((100 - crop.loss_percentage) / 100)
            planting_area = adjusted_harvest / crop.yield_per_unit

            # Retorna o resultado no formato JSON
            return JsonResponse({
                "adjusted_harvest": round(adjusted_harvest, 2),
                "planting_area": round(planting_area, 2),
                "yield_unit": crop.yield_unit
            })
        except (ValueError, KeyError) as e:
            return JsonResponse({"error": f"Erro nos dados fornecidos: {str(e)}"}, status=400)

    return JsonResponse({"error": "Método não permitido."}, status=405)