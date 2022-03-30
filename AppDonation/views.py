from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Accounts.models import Profile

from AppDonation.forms import DonationForm,DonationUpdateForm
from AppDonation.models import Donations
# Create your views here.

@login_required
def Dontaion(request):
    diction = {}
    donation_form = DonationForm()
    if request.user.profile.userType == 1:
        if request.method == 'POST':
            donation_form = DonationForm(request.POST)
            if donation_form.is_valid():
                donations = donation_form.save(commit = False)
                donations.user = request.user
                donations.district = request.user.profile.district
                donation_form.save()
                return HttpResponseRedirect(reverse('accounts:userProfile'))
        donation_form = DonationForm()
        diction = {'title':'This is donation App','donation_form':donation_form}
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))
    return render(request,'Donor/donation.html',context=diction)

@login_required
def viewVolunteer(request):
    verified = False
    user = request.user
    if(user.profile.verified):
        volunteers = Profile.objects.filter(district=user.profile.district,userType=2)
        diction = {'title':'View Volunteer','volunteers':volunteers}
        return render(request,'Donor/viewVolunteer.html',context=diction)
    else:
        messages.error(request,"Your profile is not verified yet")
        return HttpResponseRedirect(reverse('accounts:userProfile'))
# @login_required
# def myDonations(request,pk):
#     # user = User.objects.get(user=request.user)
#     donations = Donations.objects.filter(user_id=pk)
#     # donations = Donations.objects.all()
#     diction = {'donations':donations}
#     return render(request,'accounts/profile.html',context=diction)

@login_required
def updateDonation(request,pk):
    donation = Donations.objects.get(pk=pk)
    form = DonationUpdateForm(instance=donation)
    if request.method=='POST':
        form = DonationForm(instance=donation,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:userProfile'))
    diction = {'form':form}
    return render(request,'Donor/donationUpdate.html',context=diction)

@login_required
def deleteDonation(request,pk):
    donation = Donations.objects.get(pk=pk)
    donation.delete()
    return HttpResponseRedirect(reverse('accounts:userProfile'))