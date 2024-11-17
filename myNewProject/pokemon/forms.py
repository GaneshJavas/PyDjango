from django import forms
from .models import PokemonViewer

class PokemonViewerForm(forms.Form):
    my_pokemon = forms.ModelChoiceField(queryset=PokemonViewer.objects.all(), label="Select your choice")


class PokemonViewerType(forms.Form):
    pokemon_type = forms.ModelChoiceField(queryset=PokemonViewer.objects.all().values('poke_type').distinct(),label='Select Your Type')

