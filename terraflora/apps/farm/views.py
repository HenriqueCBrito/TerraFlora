from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Farm

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
def shopping_suggestions(request):
    return render(request, 'accounts/shopping_suggestions.html')

@login_required
def calendario(request):
    return render(request, 'accounts/farm_timetable.html')