from django import forms

from Accounts.models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ('profile_pic','profile','userType',)