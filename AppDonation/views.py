from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from AppDonation.forms import DonationForm,CategoryForm
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
                donation_form.save()
                return HttpResponse("Donation Added")
        donation_form = DonationForm()
        diction = {'title':'This is donation App','donation_form':donation_form}
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))
    return render(request,'Donor/donation.html',context=diction)