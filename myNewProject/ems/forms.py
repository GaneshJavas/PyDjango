from django import forms
from .models import Venue
from django.forms import ModelForm

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = "__all__"
        fields = ['name', 'address', 'zip_code', 'phone_no', 'web', 'email_address']
        widgets = {
            
        }