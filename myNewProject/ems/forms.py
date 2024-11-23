from django import forms
from .models import Venue, Attendees
from django.forms import ModelForm

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = "__all__"
        fields = ['name', 'address', 'zip_code', 'phone_no', 'web', 'email_address']
        labels = {
            'name': '', 
            'address': '', 
            'zip_code': '', 
            'phone_no': '', 
            'web': '', 
            'email_address': ''
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Venue Name' }), 
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Venue Address' }), 
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Zip Code' }), 
            'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number' }), 
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Website' }), 
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id' })
        }

class AttendeesForm(ModelForm):
    class Meta:
        model = Attendees
        fields = "__all__"