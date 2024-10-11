from django.urls import path
from .views import register_crop, crop_detail, crop_list

urlpatterns = [
    path('crops/register/', register_crop, name='register_crop'),
    path('crops/<int:crop_id>/', crop_detail, name='crop_detail'),
    path('crops/', crop_list, name='crop_list'),
]
