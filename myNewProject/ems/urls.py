from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'ems-home'),
    path('events', views.event_list, name = 'event-list'),
    path('add_venue', views.add_venue, name = 'add-venue'),
]
