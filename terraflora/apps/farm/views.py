from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Farm  # Import your Farm model


# View to register a new farm
@login_required
def register_farm(request):
    if request.method == 'POST':
        farm_name = request.POST.get('farm_name')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country', 'Brazil')  # Default to Brazil if not provided
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
            user=request.user  # Associate the farm with the logged-in user
        )
        farm.save()

        messages.success(request, 'Farm registered successfully!')
        return redirect('farm_detail', farm_id=farm.id)  # Redirect to the farm detail view

    else:
        # Display the form if the request method is GET
        return render(request, 'register_farm.html')


# View to display details of a specific farm
@login_required
def farm_detail(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)  # Ensure the user owns the farm

    return render(request, 'farm_detail.html', {'farm': farm})