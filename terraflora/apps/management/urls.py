from django.urls import path
from . import views

urlpatterns = [
    # URL to render the HTML calendar page
    path('calendar/', views.calendar_view, name='calendar'),

    # Event management URLs for AJAX
    path('api/add_event/', views.add_event, name='add_event'),
    path('api/edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('api/delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('api/get_events/', views.get_events, name='get_events'),
    # Weather and AI recommendation URLs for AJAX
    path('api/get_weather/', views.fetch_weather, name='get_weather'),
]
