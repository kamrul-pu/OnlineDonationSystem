
from django.contrib.auth.models import User
from django import forms
from Accounts.models import Donor,Volunteer

class UserForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username. Letters, digits and @/./+/-/_ only.'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'e.g., palga@gmail.com'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','placeholder':'Enter password'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')

class DonorForm(forms.ModelForm):
    donorAddress = forms.CharField(label="Donor Address",widget=forms.TextInput(attrs={'type':'textarea','rows':5,'cols':20}))
    nationalId = forms.CharField(label="National ID")
    class Meta:
        model = Donor
        exclude = ('donor','isDonor',)

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        exclude = ('volunteer','isVolunteer',)