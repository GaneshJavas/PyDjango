from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, AttendeesForm
# Create your views here.
def home(request):
    return render(request,'index.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# def add_venue(request):
#     submitted = False
#     if request.method == 'POST':
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/ems/add_venue?submit=True')  
#     else:
#         form = VenueForm
#         if 'submit' in request.GET:
#             submitted = True
    
#     return render(request, 'add_venue.html', {'form': form, 'submit':submitted})

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ems/add_venue?submit=True')  
    else:
        form = VenueForm
        if 'submit' in request.GET:
            submitted = True
    
    return render(request, 'add_venue.html', {'form': form, 'submit':submitted})

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'venue_list.html', {'venues':venues})

def venue_details(request, v_id):
    venue = get_object_or_404(Venue, pk = v_id)
    return render(request, 'venue_details.html', {'venue':venue})

def add_attendee(request):
    submitted = False
    if request.method == 'POST':
        form = AttendeesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ems/add_attendee?submit=True')
    else:
        form = AttendeesForm
        if 'submit' in request.GET:
            submitted = True
    return render(request, 'add_attendee.html',{'form':form, 'submit':submitted})


def  search_venue(request):
    return render(request, 'search_venue.html' )