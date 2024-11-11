from django.contrib import admin
from .models import PokemonViewer, PokemonRating, PokemonRegion, PokemonDiscovery
# Register your models here.

# admin.site.register(PokemonViewer)

class pokemon_rating(admin.TabularInline):
    model = PokemonRating
    extra = 0

class all_pokemons(admin.ModelAdmin):
    list_display = ('id','name', 'poke_type')
    inlines = [pokemon_rating]

class pokemon_region(admin.ModelAdmin):
    list_display = ('region_name',)
    filter_horizontal = ('poke_in_my_region',)

class pokemon_discovery(admin.ModelAdmin):
    list_display = ('poke_discovered','disc_cert',)

admin.site.register(PokemonViewer,all_pokemons)
admin.site.register(PokemonRegion,pokemon_region)
admin.site.register(PokemonDiscovery,pokemon_discovery)