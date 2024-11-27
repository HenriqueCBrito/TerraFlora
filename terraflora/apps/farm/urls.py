from django.urls import path
from .views import farm_list, farm_detail, register_farm, edit_farm, delete_farm
from apps.farm.views import manage_field_areas
from . import views
urlpatterns = [
    path('', farm_list, name='farm_list'),
    path('<int:farm_id>/', farm_detail, name='farm_detail'),
    path('<int:farm_id>/edit/', edit_farm, name='edit_farm'),
    path('<int:farm_id>/delete/', delete_farm, name='delete_farm'),  # URL para deletar a fazenda
    path('register/', register_farm, name='register_farm'),  # URL para 'register_farm'
    path('field-areas/', manage_field_areas, name='manage_field_areas'),
    path('field-areas/<int:farm_id>/divide/', views.divide_field, name='divide_field'),
    path('field-areas/<int:farm_id>/adjust/', views.adjust_field_areas, name='adjust_field_areas'),
    path('field-areas/<int:area_id>/assign/', views.assign_crop_to_area, name='assign_crop_to_area'),
]
