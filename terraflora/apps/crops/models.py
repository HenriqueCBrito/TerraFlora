from django.db import models
from django.conf import settings

class Culturas(models.Model):
    CROP_TYPES = [
        ('vegetable', 'Vegetal'),
        ('fruit', 'Fruta'),
        ('grain', 'Grão'),
        ('herb', 'Erva'),
        ('flower', 'Flor'),
    ]

    # Relacionamento com o usuário
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usar o modelo de usuário customizado
        on_delete=models.CASCADE,
        related_name='cultures'  # Renamed to maintain consistency
    )
    
    # Nome da cultura
    name = models.CharField(max_length=100, help_text='Nome da cultura, como tomate, alface, etc.')
    
    # Tipo de cultura
    crop_type = models.CharField(max_length=20, choices=CROP_TYPES, help_text='Tipo de cultura (vegetal, fruta, grão, erva, flor).')
    
    # Estação de plantio
    planting_season = models.CharField(max_length=100, help_text='Estação do ano ideal para o plantio, como primavera ou verão.')
    
    # Estação de colheita
    harvest_season = models.CharField(max_length=100, help_text='Estação do ano em que a cultura deve ser colhida.')
    
    # Condições de crescimento
    growing_conditions = models.TextField(help_text='Condições necessárias para o crescimento da cultura, como solo, luz e irrigação.')
    
    # Plantas compatíveis
    compatible_plants = models.TextField(help_text='Plantas que são compatíveis para o cultivo conjunto.')
    
    # Pragas comuns
    common_pests = models.TextField(help_text='Pragas comuns que podem afetar esta cultura.')
    
    # Necessidades de irrigação
    watering_needs = models.CharField(max_length=100, help_text='Necessidades de irrigação da cultura, como "regular" ou "moderada".')
    
    # Exposição ao sol
    sun_exposure = models.CharField(max_length=100, help_text='Exposição ao sol necessária, como "sol pleno" ou "sombra parcial".')
    
    # Notas adicionais
    notes = models.TextField(blank=True, help_text='Notas adicionais sobre a cultura.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cultura'  # Singular name
        verbose_name_plural = 'Culturas'  # Plural name

