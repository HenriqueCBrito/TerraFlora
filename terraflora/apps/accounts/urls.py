from django.urls import path
from .views import register, user_login, logoff, home, menu

urlpatterns = [
    path('', home, name='home'),  # Rota para a página inicial (home)
    path('menu/', menu, name='menu'),  # Rota para o menu
    path('register/', register, name='register'),  # Rota para registro
    path('login/', user_login, name='login'),  # Rota para login
    path('logout/', logoff, name='logout'),  # Rota para logout
]
