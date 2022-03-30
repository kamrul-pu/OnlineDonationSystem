from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AppDonation.models import Donations
from Accounts.models import Profile
# Create your views here.

@login_required
def viewDonors(request):
    verified = False
    user = request.user
    if(user.profile.verified):
        donors = Profile.objects.filter(district=user.profile.district,userType=1)
        diction = {'title':'View Donors','donors':donors,'verified':True}
        return render(request,'Volunteer/donors.html',context=diction)
    else:
        messages.error(request,"Your profile is not verified yet")
        return HttpResponseRedirect(reverse('accounts:userProfile'))

@login_required
def viewDonations(request,pk):
    # donations = Donations.objects.filter(district = request.user.profile.district)
    profile = User.objects.get(pk=pk)
    print("Profile = ",profile)
    # donations = Donations.objects.raw(f"select * from AppDonation_donations where(user_id={pk});")
    # donations = Donations.objects.filter(user = profile)
    donations = Donations.objects.filter(user_id = pk)
    print("Donations = ",donations)
    diction = {'title':'View Donations','donations':donations}
    return render(request,'Volunteer/viewDonations.html',context = diction)
