from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm
# Create your views here.
def home(request):
    return render(request,'index.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

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