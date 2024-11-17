from django.shortcuts import render, get_object_or_404
from .models import PokemonViewer, PokemonRegion
from .forms import  PokemonViewerType, PokemonViewerForm

# Create your views here.
def pokemon_world(request):
    pokemons = PokemonViewer.objects.all()
    return render(request, 'pokemon/pokemon_world.html',{'pokemons': pokemons})

def poke_details(request, poke_id):
    poke_del = get_object_or_404(PokemonViewer, pk=poke_id)
    return render(request, 'pokemon/pokemon_details.html',{'poke_details':poke_del})

# def search_view(request):
#     region = None
#     # Checking whether the request method is POST or GET
#     if request.method == 'POST':
#        form = PokemonViewerForm(request.POST) 
#        print(form)
#        print(request.POST.get('my_pokemon'))

#        # Checking form validation
#        if form.is_valid():
#            # data cleaning
#            my_pokemons = form.cleaned_data['my_pokemon']
#            print(my_pokemons)
#            region = PokemonRegion.objects.filter(poke_in_my_region = my_pokemons)
#     else: 
#         form = PokemonViewerForm()
    
#     return render(request, 'pokemon/search_palatte.html',{'form':form,'region': region})
    

def search_view(request):
    region = None
    # Checking whether the request method is POST or GET
    if request.method == 'POST': 
       form = PokemonViewerType(request.POST)
       print(form)
       print(request.POST.get('pokemon_type'))
       # Checking form validation
       if form.is_valid():
           # data cleaning
           my_pokemons = form.cleaned_data['pokemon_type']
           print(my_pokemons)
           region = PokemonViewer.objects.filter(poke_type=my_pokemons['poke_type'])
    else: 
        form = PokemonViewerType()
    
    return render(request, 'pokemon/search_palatte.html',{'form':form,'region': region})


# search -> region -> pokemon
# search -> type -> pokemon
# search -> name -> region