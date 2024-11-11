<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Culturas

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

>>>>>>> guilherme_vinicius
