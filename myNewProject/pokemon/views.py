from django.shortcuts import render
from .models import PokemonViewer

# Create your views here.
def pokemon_world(request):
    pokemons = PokemonViewer.objects.all()
    return render(request, 'pokemon/pokemon_world.html',{'pokemons': pokemons})