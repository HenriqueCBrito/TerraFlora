from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from apps.management.models import Storage
from .models import Farm, FieldArea

# View to register a new farm
@login_required
def register_farm(request):
    if request.method == 'POST':
        farm_name = request.POST.get('farm_name')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country', 'Brazil')
        size = request.POST.get('size')
        size_unit = request.POST.get('size_unit')

        # Basic validation for required fields
        if not all([farm_name, street, home_number, city, state, size, size_unit]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'register_farm.html')

        # Create and save the new farm
        farm = Farm(
            farm_name=farm_name,
            street=street,
            home_number=home_number,
            city=city,
            state=state,
            country=country,
            size=size,
            size_unit=size_unit,
            user=request.user
        )
        farm.save()

        messages.success(request, 'Farm registered successfully!')
        return redirect(reverse('farm_detail', args=[farm.id]))  # Correção aqui

    else:
        # Display the form if the request method is GET
       return render(request, 'farm/register_farm.html')


# View to display details of a specific farm
@login_required
def farm_detail(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)  # Ensure the user owns the farm
    return render(request, 'farm/farm_detail.html', {'farm': farm})

@login_required
def farm_list(request):
    farms = Farm.objects.filter(user=request.user)  # Filtra as fazendas do usuário logado
    return render(request, 'farm/farm_list.html', {'farms': farms})

@login_required
def edit_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)

    if request.method == 'POST':
        farm_name = request.POST.get('farm_name')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        size = request.POST.get('size')
        size_unit = request.POST.get('size_unit')

        # Validação básica
        if not all([farm_name, street, home_number, city, state, size, size_unit]):
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'farm/edit_farm.html', {'farm': farm})

        # Atualiza os dados da fazenda
        farm.farm_name = farm_name
        farm.street = street
        farm.home_number = home_number
        farm.city = city
        farm.state = state
        farm.country = country
        farm.size = size
        farm.size_unit = size_unit
        farm.save()

        messages.success(request, 'Fazenda atualizada com sucesso!')
        return redirect('farm_detail', farm_id=farm.id)

    # Renderiza o template de edição de fazenda com os dados atuais da fazenda
    return render(request, 'farm/edit_farm.html', {'farm': farm})

@login_required
def delete_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)
    
    if request.method == 'POST':
        farm.delete()
        messages.success(request, 'Fazenda excluída com sucesso!')
        return redirect('farm_list')

    return render(request, 'farm/delete_farm.html', {'farm': farm})

@login_required
def view_field(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)
    field_areas = farm.field_areas.all()
    crops = Storage.objects.filter(user=request.user, category='Seed')

    # Handle Divide Field
    if request.method == 'POST' and 'num_areas' in request.POST:
        num_areas = int(request.POST.get('num_areas'))
        if num_areas <= 0 or num_areas > 100:
            messages.error(request, 'Insira um número válido de áreas (1-100).')
        else:
            total_size = farm.size
            area_size = total_size / num_areas
            farm.field_areas.all().delete()
            for i in range(1, num_areas + 1):
                FieldArea.objects.create(farm=farm, name=f"Área {i}", size=area_size)
            messages.success(request, f"Fazenda dividida em {num_areas} partes iguais!")
        return redirect('view_field', farm_id=farm_id)

    # Handle Adjust Field Areas
    if request.method == 'POST' and 'adjust_areas' in request.POST:
        adjustments = {}
        for area in field_areas:
            new_size = request.POST.get(f'size_{area.id}')
            if new_size:
                new_size = float(new_size)
                if new_size != area.size:
                    adjustments[area.id] = new_size

        if adjustments:
            total_adjustment = sum(adjustments.values()) - sum(area.size for area in field_areas)
            if total_adjustment > 0:  # Increasing total size
                messages.error(request, "A soma das áreas excede o tamanho total da fazenda.")
            else:
                for area_id, new_size in adjustments.items():
                    area = field_areas.get(id=area_id)
                    area.size = new_size
                    area.save()
                messages.success(request, 'Tamanhos das áreas ajustados com sucesso!')

        return redirect('view_field', farm_id=farm_id)

    # Handle Assign Crop to Area
    if request.method == 'POST' and 'assign_crop' in request.POST:
        area_id = request.POST.get('area_id')
        crop_id = request.POST.get('crop')
        area = get_object_or_404(FieldArea, id=area_id, farm=farm)
        crop = get_object_or_404(Storage, id=crop_id, user=request.user)
        required_quantity = area.size / crop.recommended_area
        if crop.quantity < required_quantity:
            messages.error(request, f"Quantidade insuficiente de {crop.product_name} no armazenamento.")
        else:
            area.crop = crop
            area.save()
            messages.success(request, f"{crop.product_name} atribuído à {area.name}!")
        return redirect('view_field', farm_id=farm_id)

    return render(request, 'farm/view_field.html', {
        'farm': farm,
        'field_areas': field_areas,
        'crops': crops,
    })