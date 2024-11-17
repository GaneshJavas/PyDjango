from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.TextField('Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=6)
    phone_no = models.CharField('Phone Number', max_length=15)
    web = models.URLField('Website',blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name
    
class Attendees(models.Model):
    f_name = models.CharField('First Name', max_length= 15)
    l_name = models.CharField('Last Name', max_length=15)
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.f_name
    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField('Venue', max_length=120)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    # manager = models.CharField('Manager', max_length=60)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField('Description', blank=True)
    attendees = models.ManyToManyField(Attendees, blank=True)

    def __str__(self):
        return self.name
    

