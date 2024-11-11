from django.urls import path
<<<<<<< HEAD
from . import views  # Importando as views

urlpatterns = [
    # url pra exibir o formulario de cadastro
    path('cadastrar/', views.cadastrar_fazenda, name='cadastrar_fazenda'),

    # url pra exibir a pagina de sucesso dps do cadastro
    path('sucesso/', views.sucesso, name='fazenda_sucesso'),
=======
from .views import farm_list, farm_detail, register_farm, edit_farm, delete_farm, shopping_suggestions, calendario,get_events

urlpatterns = [
    path('', farm_list, name='farm_list'),
    path('<int:farm_id>/', farm_detail, name='farm_detail'),
    path('<int:farm_id>/edit/', edit_farm, name='edit_farm'),
    path('<int:farm_id>/delete/', delete_farm, name='delete_farm'),  # URL para deletar a fazenda
    path('register/', register_farm, name='register_farm'),  # URL para 'register_farm'
    path('meus_dados/', shopping_suggestions, name='user_data'),
    path('calendario/', calendario, name='calendar'),
    path('api/get_events/', get_events, name='get_events'),

>>>>>>> guilherme_vinicius
]
