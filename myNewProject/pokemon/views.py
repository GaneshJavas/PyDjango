from django.shortcuts import render

# Create your views here.
def pokemon_world(request):
    return render(request, 'pokemon/pokemon_world.html')