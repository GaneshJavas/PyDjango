
from django.urls import path
from . import views

#localhost:8000/pokemonhome
urlpatterns = [
    path('', views.pokemon_world, name = 'pokemon_world'),
    path('id=<int:poke_id>/', views.poke_details, name = "poke_details")
]
