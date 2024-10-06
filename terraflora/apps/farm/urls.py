from django.urls import path
from . import views  # Importando as views

urlpatterns = [
    # url pra exibir o formulario de cadastro
    path('cadastrar/', views.cadastrar_fazenda, name='cadastrar_fazenda'),

    # url pra exibir a pagina de sucesso dps do cadastro
    path('sucesso/', views.sucesso, name='fazenda_sucesso'),
]
