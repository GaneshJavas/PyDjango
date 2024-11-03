from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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


class PokemonRating(models.Model):
    poke = models.ForeignKey(PokemonViewer, on_delete=models.CASCADE, related_name="rating")
    poke_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.poke_user.username} Rated for {self.poke.name}'

class PokemonRegion(models.Model):
    poke_in_my_region = models.ManyToManyField(PokemonViewer, related_name="region")
    region_name = models.CharField(max_length=50)

    def __str__(self):
        return self.region_name
    
class PokemonDiscovery(models.Model):
    poke_discovered = models.OneToOneField(PokemonViewer, on_delete=models.CASCADE, related_name="disc")
    discovery_date = models.DateTimeField(default=timezone.now())
    disc_cert = models.CharField(max_length=10)

    def __str__(self):
        return f'Certificate for {self.poke_discovered.name}'
