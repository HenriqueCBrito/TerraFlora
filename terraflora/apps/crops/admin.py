from django.contrib import admin
from .models import Culturas

class CulturasAdmin(admin.ModelAdmin):
    list_display = ('name', 'crop_type', 'planting_season', 'harvest_season', 'user')
    search_fields = ('name', 'crop_type')
    list_filter = ('crop_type',)

    # Optional: If you want to ensure the user is set when creating a crop
    def save_model(self, request, obj, form, change):
        if not obj.user:  # Check if user is not already set
            obj.user = request.user  # Set the user to the current logged-in user
        super().save_model(request, obj, form, change)

admin.site.register(Culturas, CulturasAdmin)
