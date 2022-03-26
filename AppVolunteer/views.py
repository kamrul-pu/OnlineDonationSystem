from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from AppDonation.models import Donations
from Accounts.models import Profile
# Create your views here.

@login_required
def viewDonors(request):
    user = request.user
    donors = Profile.objects.filter(district=user.profile.district,userType=1)
    diction = {'title':'View Donors','donors':donors}
    return render(request,'Volunteer/donors.html',context=diction)

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
