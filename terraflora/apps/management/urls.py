from django.urls import path
from . import views

urlpatterns = [
    # URL to render the HTML calendar page
    path('calendar/', views.calendar_view, name='calendar'),

    # Event management URLs for AJAX
    path('api/add_event/', views.add_event, name='add_event'),
    path('api/edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('api/delete_event/<int:event_id>/', views.delete_event, name='delete_event'),

    # Weather and AI recommendation URLs for AJAX
    path('api/get_weather/', views.fetch_weather, name='get_weather'),
    path('storage/', views.list_storage, name='list_storage'),  # Listar produtos
    path('storage/add/', views.add_storage, name='add_storage'),  # Adicionar produto
    path('storage/update/<int:storage_id>/', views.update_storage, name='update_storage'),  # Editar produto
    path('storage/delete/<int:storage_id>/', views.delete_storage, name='delete_storage'),  # Excluir produto
    path('storage/manage/', views.manage_storage, name='manage_storage'),
    path('shopping/', views.shopping_list, name='shopping_list'), 
    path('explore/', views.explore, name='explore'),  
]

