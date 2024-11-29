from django.db import models
from django.conf import settings

from apps.management.models import Storage

# Class Farm
class Farm(models.Model):
    # Nome da fazenda
    farm_name = models.CharField(max_length=255)

    # Endereço da fazenda
    street = models.CharField(max_length=255)
    home_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Brazil')

    # Tamanho da fazenda
    size = models.FloatField()

    # Unidade de medida para o tamanho
    SIZE_UNITS = [
        ('m2', 'Metros Quadrados'),
        ('ac', 'Acres'),
        ('ha', 'Hectares'),
    ]
    size_unit = models.CharField(max_length=2, choices=SIZE_UNITS)

    # Relacionamento com o usuário
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usar o modelo de usuário customizado
        on_delete=models.CASCADE,
        related_name='farms'
    )

    def __str__(self):
        return f"{self.farm_name}, {self.city} - {self.state}"

    class Meta:
        verbose_name = 'Farm'
        verbose_name_plural = 'Farms'
        
class FieldArea(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='field_areas')
    name = models.CharField(max_length=100, help_text="Nome da área.")
    size = models.FloatField(help_text="Tamanho da área em m².")
    crop = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, blank=True, related_name='field_areas')
    notes = models.TextField(blank=True, help_text="Notas adicionais sobre esta área.")

    def __str__(self):
        return f"{self.name} - {self.farm.farm_name}"