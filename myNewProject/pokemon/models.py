from django.db import models
from django.utils import timezone
# Create your models here.

class PokemonViewer(models.Model):
    pokemon_type_choice =[
        ('LE','Legendary'),
        ('EL','Electric'),
        ('GR','Grass'),
        ('PY','Psychic'),
        ('FI','Fire'),
        ('WR','Water'),
        ('AR','Air'),
        ('GH','Ghost')
    ] 

    name = models.CharField(max_length=50)
    pimage = models.ImageField(upload_to='pokeimg/')
    dob = models.DateTimeField(default=timezone.now)
    poke_type = models.CharField(max_length=2, choices=pokemon_type_choice,default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
