from django.db import models
from django.conf import settings
from apps.crops.models import Culturas  

class Event(models.Model):
    crop = models.ForeignKey(
        Culturas,
        on_delete=models.CASCADE,
        related_name='events'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events'
    )
    title = models.CharField(max_length=100, help_text="Título da tarefa, como Plantar ou Colher")
    task_type = models.CharField(
        max_length=50,
        choices=[
            ('Planting', 'Plantio'),
            ('Harvesting', 'Colheita'),
            ('Watering', 'Irrigação'),
            ('Pruning', 'Poda'),
            ('Soil Management', 'Remanejo do Solo')
        ],
        help_text="Tipo de tarefa para a cultura."
    )
    description = models.TextField(blank=True, help_text="Descrição ou notas adicionais sobre a tarefa.")
    start_date = models.DateTimeField(help_text="Data e hora de início do evento.")
    end_date = models.DateTimeField(help_text="Data e hora de término do evento.")
    priority = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Baixa'),
            ('Medium', 'Média'),
            ('High', 'Alta')
        ],
        default='Medium',
        help_text="Prioridade da tarefa."
    )
    completed = models.BooleanField(default=False, help_text="Indica se a tarefa foi concluída.")
    weather_summary = models.CharField(max_length=255, blank=True, help_text="Resumo das condições meteorológicas.")

    def __str__(self):
        return f"{self.title} - {self.crop.name}"

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-start_date']

class CropSuggestion(models.Model):
    name = models.CharField(max_length=100, help_text="Nome do item (semente, fertilizante, etc.).")
    category = models.CharField(
        max_length=50,
        choices=[
            ('Seed', 'Semente'),
            ('Fertilizer', 'Fertilizante'),
            ('Pesticide', 'Pesticida')
        ],
        help_text="Categoria do item."
    )
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Custo médio por unidade.")
    unit = models.CharField(max_length=50, help_text="Unidade de medida (kg, litros, etc.).")
    recommended_area = models.FloatField(help_text="Área recomendada para uso deste item (em m²).")

    def __str__(self):
        return f"{self.name} ({self.category})"
    
class Storage(models.Model):
    PRODUCT_CATEGORIES = [
        ('Seed', 'Semente'),
        ('Fertilizer', 'Fertilizante'),
        ('Pesticide', 'Pesticida'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='storages',
        help_text="Usuário que possui este armazenamento."
    )
    culture = models.ForeignKey(
        Culturas,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Cultura associada a este armazenamento (se aplicável)."
    )
    product_name = models.CharField(max_length=100, help_text="Nome do produto.")
    category = models.CharField(max_length=20, choices=PRODUCT_CATEGORIES, help_text="Categoria do produto.")
    quantity = models.FloatField(help_text="Quantidade do produto em estoque.")
    unit = models.CharField(max_length=50, help_text="Unidade de medida (kg, litros, etc.).")
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Custo médio por unidade.")
    recommended_area = models.FloatField(help_text="Área recomendada para uso deste produto (em m²).", null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, help_text="Data da última atualização.")

    def __str__(self):
        return f"{self.product_name} ({self.category}) - {self.quantity} {self.unit}"