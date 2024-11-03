from django.contrib import admin
from .models import PokemonViewer, PokemonRating, PokemonRegion, PokemonDiscovery
# Register your models here.

# admin.site.register(PokemonViewer)

class pokemon_rating(admin.TabularInline):
    model = PokemonRating
    extra = 2

class all_pokemons(admin.ModelAdmin):
    display_pokemon = ('id','name', 'poke_type')
    inlines = [pokemon_rating]

class pokemon_region(admin.ModelAdmin):
    display_region = ('Name',)
    filter_horizontal = ('poke_in_my_region',)

class pokemon_discovery(admin.ModelAdmin):
    display_cert = ('Certificate',)

admin.site.register(PokemonViewer,all_pokemons)
admin.site.register(PokemonRegion,pokemon_region)
admin.site.register(PokemonDiscovery,pokemon_discovery)