from django.contrib import admin
from django.urls import path
from apps.accounts import views  # Ajuste o caminho da importação se necessário

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.user_login, name='login'),  # A URL raiz redireciona para o login
    path('home/', views.home, name='home'),  # Página home protegida por login
    path('menu/', views.menu, name='menu'),  # Página de menu
    path('register/', views.register, name='register'),  # Página de registro
    path('login/', views.user_login, name='login'),  # Página de login
    path('logout/', views.logoff, name='logout'),  # Página de logout
    path('imersao/', views.imersao, name='imersao'),
]
