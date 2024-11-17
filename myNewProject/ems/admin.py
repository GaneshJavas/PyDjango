from django.contrib import admin
from .models import Event, Attendees, Venue
# Register your models here.

# admin.site.register(Event)
admin.site.register(Attendees)
# admin.site.register(Venue)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_no')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date','description', 'manager')
    list_display = ('name', 'venue', 'event_date')
    ordering = ('event_date',)
    list_filter = ('event_date', 'venue')
