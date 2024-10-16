# apps/farm/urls.py
from django.urls import path
from .views import farm_list, farm_detail

urlpatterns = [
    path('', farm_list, name='farm_list'),  # Certifique-se de que o nome é 'farm_list'
    path('<int:farm_id>/', farm_detail, name='farm_detail'),
]
