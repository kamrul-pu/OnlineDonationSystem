import imp
from django import forms
from AppDonation.models import Category,Donations

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donations
        # fields = "__all__"
        exclude = ('user','district','supplied',)