from django.contrib import admin
from django.urls import path, include
from apps.accounts import views  # Mantendo o import correto com base na estrutura de pastas

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),  # Página inicial protegida por login
    path('accounts/', include('apps.accounts.urls')),  # Inclui as URLs da aplicação 'accounts'
    path('farms/', include('apps.farm.urls')),  # Inclui as URLs da aplicação 'farms'
    path('menu/', views.menu, name='menu'),  # Página personalizada de menu
]
