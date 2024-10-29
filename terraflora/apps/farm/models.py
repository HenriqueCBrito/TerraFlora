from django.db import models
from django.conf import settings

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


class Event(models.Model):
    title = models.CharField(max_length=255)
    culture_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
