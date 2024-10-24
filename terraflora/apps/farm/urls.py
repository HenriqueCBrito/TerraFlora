from django.urls import path
from .views import farm_list, farm_detail, register_farm, edit_farm, delete_farm

urlpatterns = [
    path('', farm_list, name='farm_list'),
    path('<int:farm_id>/', farm_detail, name='farm_detail'),
    path('<int:farm_id>/edit/', edit_farm, name='edit_farm'),
    path('<int:farm_id>/delete/', delete_farm, name='delete_farm'),  # URL para deletar a fazenda
    path('register/', register_farm, name='register_farm'),  # URL para 'register_farm'
]
