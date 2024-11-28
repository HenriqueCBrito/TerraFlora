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
            # Convert farm size to square meters
            total_size = farm.size
            if farm.size_unit == 'ac':
                total_size *= 4046.86  # Convert acres to m²
            elif farm.size_unit == 'ha':
                total_size *= 10000  # Convert hectares to m²

            # Calculate area size and divide
            area_size = total_size / num_areas
            farm.field_areas.all().delete()
            for i in range(1, num_areas + 1):
                FieldArea.objects.create(farm=farm, name=f"Área {i}", size=area_size)
            messages.success(request, f"Fazenda dividida em {num_areas} partes iguais!")
        return redirect('view_field', farm_id=farm_id)

    # Adjust Field Areas
    if request.method == 'POST' and 'adjust_value' in request.POST:
        area_id = int(request.POST.get('adjust_area'))
        adjustment = float(request.POST.get('adjust_value'))
        area = get_object_or_404(FieldArea, id=area_id, farm=farm)

        if adjustment > 0:  # Making the area bigger
            reduce_area_id = request.POST.get('reduce_area')
            if not reduce_area_id:
                messages.error(request, 'Selecione uma área para reduzir.')
                return redirect('view_field', farm_id=farm_id)
            reduce_area = get_object_or_404(FieldArea, id=reduce_area_id, farm=farm)
            if reduce_area.size < adjustment:
                messages.error(request, f"A área {reduce_area.name} não possui tamanho suficiente para redução.")
                return redirect('view_field', farm_id=farm_id)
            reduce_area.size -= adjustment
            reduce_area.save()

        elif adjustment < 0:  # Making the area smaller
            increase_area_id = request.POST.get('increase_area')
            if increase_area_id:  # Only proceed if the user selected an area to increase
                increase_area = get_object_or_404(FieldArea, id=increase_area_id, farm=farm)
                increase_area.size += abs(adjustment)
                increase_area.save()
            else:
                # No increase area selected; log information or add a message
                messages.info(request, f"A área {area.name} foi reduzida. Considere aumentar outra área.")

        # Apply adjustment to the selected area
        if area.size + adjustment <= 0:
            messages.error(request, f"Ajuste inválido. A área {area.name} não pode ter tamanho menor ou igual a zero.")
            return redirect('view_field', farm_id=farm_id)
        area.size += adjustment
        area.save()
        messages.success(request, f"Ajuste realizado com sucesso para a área {area.name}.")
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