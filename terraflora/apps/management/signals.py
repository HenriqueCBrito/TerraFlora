from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CropSuggestion

@receiver(post_migrate)
def populate_crop_suggestions(sender, **kwargs):
    if CropSuggestion.objects.exists():
        return  # Avoid duplicate entries if suggestions already exist

    suggestions = [
        # Seeds
        {'name': 'Semente de Milho', 'category': 'Seed', 'average_cost': 20.00, 'unit': 'kg', 'recommended_area': 100},
        {'name': 'Semente de Tomate', 'category': 'Seed', 'average_cost': 25.00, 'unit': 'kg', 'recommended_area': 80},
        {'name': 'Semente de Cenoura', 'category': 'Seed', 'average_cost': 15.00, 'unit': 'kg', 'recommended_area': 120},
        {'name': 'Semente de Alface', 'category': 'Seed', 'average_cost': 10.00, 'unit': 'kg', 'recommended_area': 50},
        {'name': 'Semente de Feijão', 'category': 'Seed', 'average_cost': 18.00, 'unit': 'kg', 'recommended_area': 90},
        {'name': 'Semente de Melancia', 'category': 'Seed', 'average_cost': 30.00, 'unit': 'kg', 'recommended_area': 150},
        {'name': 'Semente de Abóbora', 'category': 'Seed', 'average_cost': 22.00, 'unit': 'kg', 'recommended_area': 110},
        {'name': 'Semente de Morango', 'category': 'Seed', 'average_cost': 35.00, 'unit': 'kg', 'recommended_area': 70},
        {'name': 'Semente de Abacaxi', 'category': 'Seed', 'average_cost': 40.00, 'unit': 'kg', 'recommended_area': 200},
        {'name': 'Semente de Beterraba', 'category': 'Seed', 'average_cost': 12.00, 'unit': 'kg', 'recommended_area': 100},

        # Fertilizers
        {'name': 'Fertilizante NPK 10-10-10', 'category': 'Fertilizer', 'average_cost': 50.00, 'unit': 'kg', 'recommended_area': 200},
        {'name': 'Adubo Orgânico', 'category': 'Fertilizer', 'average_cost': 40.00, 'unit': 'kg', 'recommended_area': 150},
        {'name': 'Fertilizante Solúvel', 'category': 'Fertilizer', 'average_cost': 60.00, 'unit': 'kg', 'recommended_area': 250},

        # Pesticides
        {'name': 'Pesticida Orgânico', 'category': 'Pesticide', 'average_cost': 30.00, 'unit': 'litro', 'recommended_area': 300},
        {'name': 'Herbicida Biológico', 'category': 'Pesticide', 'average_cost': 35.00, 'unit': 'litro', 'recommended_area': 250},
        {'name': 'Fungicida Natural', 'category': 'Pesticide', 'average_cost': 40.00, 'unit': 'litro', 'recommended_area': 200},
    ]

    for suggestion in suggestions:
        CropSuggestion.objects.get_or_create(
            name=suggestion['name'],
            category=suggestion['category'],
            average_cost=suggestion['average_cost'],
            unit=suggestion['unit'],
            recommended_area=suggestion['recommended_area']
        )
