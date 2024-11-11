from apps.accounts.models import CustomUser
from apps.crops.models import Culturas

def add_example_crops(user):
    example_crops = [
            # Vegetais
    {
        'name': 'Tomate',
        'crop_type': 'vegetable',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solo bem drenado, pleno sol, rega regular',
        'compatible_plants': 'Manjericão, alho',
        'common_pests': 'Pulgões, mosca-branca',
        'watering_needs': 'Moderada',
        'sun_exposure': 'Sol pleno',
        'notes': 'O tomate é sensível a baixas temperaturas e prefere climas quentes. É ideal para ser plantado em locais com boa exposição solar.'
    },
    {
        'name': 'Alface',
        'crop_type': 'vegetable',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solo rico em matéria orgânica, sol ou sombra parcial',
        'compatible_plants': 'Cenoura, rabanete',
        'common_pests': 'Lesmas, caracóis',
        'watering_needs': 'Frequente',
        'sun_exposure': 'Sombra parcial',
        'notes': 'A alface precisa de solo sempre úmido, mas não encharcado. Prefere temperaturas amenas para crescer de forma saudável.'
    },

    # Frutas
    {
        'name': 'Morango',
        'crop_type': 'fruit',
        'planting_season': 'Outono',
        'harvest_season': 'Primavera',
        'growing_conditions': 'Solo ácido e bem drenado, irrigação regular',
        'compatible_plants': 'Espinafre, alho',
        'common_pests': 'Pulgões, ácaros',
        'watering_needs': 'Regular',
        'sun_exposure': 'Sol pleno',
        'notes': 'O morango é uma fruta que se adapta bem a climas temperados e precisa de uma boa quantidade de sol para crescer.'
    },
    {
        'name': 'Maçã',
        'crop_type': 'fruit',
        'planting_season': 'Inverno',
        'harvest_season': 'Outono',
        'growing_conditions': 'Solo fértil e bem drenado, clima frio a temperado',
        'compatible_plants': 'Cebola, alho',
        'common_pests': 'Lagartas, pulgões',
        'watering_needs': 'Moderada',
        'sun_exposure': 'Sol pleno',
        'notes': 'As macieiras precisam de um período de frio para quebrar a dormência e florescer adequadamente na primavera.'
    },

    # Grãos
    {
        'name': 'Milho',
        'crop_type': 'grain',
        'planting_season': 'Primavera',
        'harvest_season': 'Outono',
        'growing_conditions': 'Solo fértil e bem irrigado, alta exposição ao sol',
        'compatible_plants': 'Feijão, abóbora',
        'common_pests': 'Lagartas, besouros',
        'watering_needs': 'Regular',
        'sun_exposure': 'Sol pleno',
        'notes': 'O milho é uma planta que precisa de muito espaço e se desenvolve melhor em solos bem nutridos e com bastante sol.'
    },
    {
        'name': 'Arroz',
        'crop_type': 'grain',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solos alagados, clima quente e úmido',
        'compatible_plants': 'Feijão-de-corda',
        'common_pests': 'Lagartas, gafanhotos',
        'watering_needs': 'Alta',
        'sun_exposure': 'Sol pleno',
        'notes': 'O arroz precisa de muita água para crescer, por isso é cultivado em áreas alagadas e irrigadas.'
    },

    # Ervas
    {
        'name': 'Manjericão',
        'crop_type': 'herb',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solo bem drenado, temperatura quente',
        'compatible_plants': 'Tomate, pimentão',
        'common_pests': 'Pulgões, cochonilhas',
        'watering_needs': 'Moderada',
        'sun_exposure': 'Sol pleno',
        'notes': 'O manjericão é uma erva aromática que prefere temperaturas quentes e solo seco entre regas.'
    },
    {
        'name': 'Hortelã',
        'crop_type': 'herb',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solo úmido e rico em nutrientes',
        'compatible_plants': 'Repolho, brócolis',
        'common_pests': 'Ácaros, lesmas',
        'watering_needs': 'Frequente',
        'sun_exposure': 'Sombra parcial',
        'notes': 'A hortelã é uma erva que se espalha rapidamente e prefere solo úmido e temperaturas amenas.'
    },

    # Flores
    {
        'name': 'Girassol',
        'crop_type': 'flower',
        'planting_season': 'Primavera',
        'harvest_season': 'Verão',
        'growing_conditions': 'Solo bem drenado, muita luz solar',
        'compatible_plants': 'Milho, abóbora',
        'common_pests': 'Pulgões, lagartas',
        'watering_needs': 'Moderada',
        'sun_exposure': 'Sol pleno',
        'notes': 'Os girassóis precisam de muita luz solar e solos bem drenados para crescerem fortes e saudáveis.'
    },
    {
        'name': 'Rosa',
        'crop_type': 'flower',
        'planting_season': 'Outono',
        'harvest_season': 'Primavera',
        'growing_conditions': 'Solo bem drenado, rega moderada',
        'compatible_plants': 'Alho, lavanda',
        'common_pests': 'Pulgões, ácaros',
        'watering_needs': 'Moderada',
        'sun_exposure': 'Sol pleno',
        'notes': 'As rosas são sensíveis a doenças fúngicas e devem ser plantadas em locais bem ventilados e ensolarados.'
    }
            
    ]

    for crop_data in example_crops:
        if not Culturas.objects.filter(user=user, name=crop_data['name']).exists():
            Culturas.objects.create(user=user, **crop_data)