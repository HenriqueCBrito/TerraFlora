from django.urls import path
from .views import register, user_login, logoff
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logoff, name='logout'),
]