from django.db import models
from django.conf import settings

# Defina as escolhas de unidades de rendimento antes do modelo
YIELD_UNITS = [
    ('kg', 'Quilogramas'),
    ('flores', 'Flores'),
    ('maços', 'Maços'),
]
class Culturas(models.Model):
    CROP_TYPES = [
        ('vegetable', 'Vegetal'),
        ('fruit', 'Fruta'),
        ('grain', 'Grão'),
        ('herb', 'Erva'),
        ('flower', 'Flor'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cultures')
    name = models.CharField(max_length=100, help_text='Nome da cultura, como tomate, alface, etc.')
    crop_type = models.CharField(max_length=20, choices=CROP_TYPES, help_text='Tipo de cultura.')
    planting_season = models.CharField(max_length=100, help_text='Estação ideal para o plantio.')
    harvest_season = models.CharField(max_length=100, help_text='Estação de colheita.')
    growing_conditions = models.TextField(help_text='Condições necessárias para o crescimento.')
    compatible_plants = models.TextField(help_text='Plantas compatíveis.')
    common_pests = models.TextField(help_text='Pragas comuns.')
    watering_needs = models.CharField(max_length=100, help_text='Necessidades de irrigação.')
    sun_exposure = models.CharField(max_length=100, help_text='Exposição ao sol necessária.')
    notes = models.TextField(blank=True, help_text='Notas adicionais.')

    # Novos campos para calculadora
    loss_percentage = models.FloatField(default=0.0, help_text='Percentual médio de perda no cultivo (%).')
    yield_per_unit = models.FloatField(default=0.0, help_text='Rendimento típico por unidade plantada.')
    yield_unit = models.CharField(max_length=20, choices=YIELD_UNITS, default='kg', help_text='Unidade de rendimento.')

    def save(self, *args, **kwargs):
        # Define valores padrão com base no tipo de cultura
        if not self.loss_percentage:
            self.loss_percentage = self.get_default_loss_percentage()
        if not self.yield_per_unit:
            self.yield_per_unit = self.get_default_yield_per_unit()
        if not self.yield_unit:
            self.yield_unit = self.get_default_yield_unit()
        super().save(*args, **kwargs)

    def get_default_loss_percentage(self):
        default_losses = {
            'vegetable': 15.0,
            'fruit': 20.0,
            'grain': 10.0,
            'herb': 10.0,
            'flower': 5.0,
        }
        return default_losses.get(self.crop_type, 15.0)

    def get_default_yield_per_unit(self):
        default_yields = {
            'vegetable': 6.0,   # Ex.: kg/m²
            'fruit': 5.0,       # Ex.: kg/m²
            'grain': 8.0,       # Ex.: kg/m²
            'herb': 10.0,       # Ex.: maços/m²
            'flower': 30.0,     # Ex.: flores/m²
        }
        return default_yields.get(self.crop_type, 6.0)

    def get_default_yield_unit(self):
        default_units = {
            'vegetable': 'kg',
            'fruit': 'kg',
            'grain': 'kg',
            'herb': 'maços',
            'flower': 'flores',
        }
        return default_units.get(self.crop_type, 'kg')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cultura'
        verbose_name_plural = 'Culturas'
