from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'ems-home'),
    path('events', views.event_list, name = 'event-list'),
    path('add_venue', views.add_venue, name = 'add-venue'),
    path('add_attendee', views.add_attendee, name = 'add-attendee'),
    path('venues', views.venue_list, name = 'venue-list'),
    path('venueid=<int:v_id>/', views.venue_details, name = 'venue-details'),
    path('search', views.search_venue, name = 'search-venue'),
]
