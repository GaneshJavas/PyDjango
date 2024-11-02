from django.shortcuts import render, get_object_or_404
from .models import PokemonViewer

# Create your views here.
def pokemon_world(request):
    pokemons = PokemonViewer.objects.all()
    return render(request, 'pokemon/pokemon_world.html',{'pokemons': pokemons})

def poke_details(request, poke_id):
    poke_del = get_object_or_404(PokemonViewer, pk=poke_id)
    return render(request, 'pokemon/pokemon_details.html',{'poke_details':poke_del})
