from django.db import migrations

def add_culturas_examples(apps, schema_editor):
    Culturas = apps.get_model('crops', 'Culturas')
    examples = [
        {
            "name": "Tomate",
            "crop_type": "vegetable",
            "planting_season": "Primavera",
            "harvest_season": "Verão",
            "growing_conditions": "Solo fértil, sol pleno, irrigação regular.",
            "compatible_plants": "Manjericão, cebola.",
            "common_pests": "Pulgões, mosca branca.",
            "watering_needs": "Regular",
            "sun_exposure": "Sol pleno",
            "notes": "Requer cuidados contra o apodrecimento do fruto."
        },
        {
            "name": "Alface",
            "crop_type": "vegetable",
            "planting_season": "Primavera",
            "harvest_season": "Verão",
            "growing_conditions": "Solo bem drenado, sombra parcial.",
            "compatible_plants": "Cenoura, rabanete.",
            "common_pests": "Lesmas, pulgões.",
            "watering_needs": "Moderada",
            "sun_exposure": "Sombra parcial",
            "notes": "Cresce rapidamente e deve ser colhida antes de florescer."
        },
        {
            "name": "Morango",
            "crop_type": "fruit",
            "planting_season": "Outono",
            "harvest_season": "Primavera",
            "growing_conditions": "Solo ácido, sol pleno, boa drenagem.",
            "compatible_plants": "Alface, espinafre.",
            "common_pests": "Lesmas, caracóis.",
            "watering_needs": "Regular",
            "sun_exposure": "Sol pleno",
            "notes": "Plantar com espaçamento adequado para evitar fungos."
        },
        {
            "name": "Cenoura",
            "crop_type": "vegetable",
            "planting_season": "Primavera",
            "harvest_season": "Outono",
            "growing_conditions": "Solo arenoso, bem drenado.",
            "compatible_plants": "Alface, tomate.",
            "common_pests": "Larvas de besouro.",
            "watering_needs": "Moderada",
            "sun_exposure": "Sol pleno",
            "notes": "Evitar o encharcamento do solo."
        },
        {
            "name": "Trigo",
            "crop_type": "grain",
            "planting_season": "Outono",
            "harvest_season": "Primavera",
            "growing_conditions": "Solo fértil e bem drenado, sol pleno.",
            "compatible_plants": "Feijão, lentilha.",
            "common_pests": "Gorgulho do trigo, ferrugem do trigo.",
            "watering_needs": "Baixa",
            "sun_exposure": "Sol pleno",
            "notes": "Precisa de um solo ligeiramente alcalino para melhor crescimento."
        },
        {
            "name": "Girassol",
            "crop_type": "flower",
            "planting_season": "Primavera",
            "harvest_season": "Verão",
            "growing_conditions": "Solo bem drenado, sol pleno.",
            "compatible_plants": "Milho, abóbora.",
            "common_pests": "Pulgões, caracóis.",
            "watering_needs": "Moderada",
            "sun_exposure": "Sol pleno",
            "notes": "Necessita de áreas abertas e bastante luminosidade."
        }
    ]

    for example in examples:
        Culturas.objects.create(**example)


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_culturas_examples),
    ]

