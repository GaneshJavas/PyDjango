from django import forms
from .models import PokemonViewer

class PokemonViewerForm(forms.Form):
    my_pokemon = forms.ModelChoiceField(queryset=PokemonViewer.objects.all(), label="Select your choice")




