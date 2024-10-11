from django.urls import path
from .views import register_farm, farm_detail

urlpatterns = [
    path('register/', register_farm, name='register_farm'),
    path('<slug:slug>/', farm_detail, name='farm_detail'),  # Assuming you use slug for farm detail
]
