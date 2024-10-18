from django.contrib import admin
from django.urls import path, include
from apps.accounts import views  # Correct import based on folder structure

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep admin URL here
    path('', views.home, name='home'),  # Página inicial protegida por login
    path('accounts/', include('apps.accounts.urls')),  # Include URLs from the 'accounts' app
    path('farms/', include('apps.farm.urls')),  # Include URLs from the 'farms' app
    path('menu/', views.menu, name='menu'),  # Página personalizada de menu
    path('crops/', include('apps.crops.urls')),
]