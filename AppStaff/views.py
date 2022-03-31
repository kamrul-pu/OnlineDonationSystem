from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from Accounts.models import Profile
from AppStaff.forms import ProfileUpdateForm

# Create your views here.

@login_required
def staff(request):
    if(request.user.is_staff):
        diction = {'title':'Staff Functionalities'}
        return render(request,'Staff/staff.html',context=diction)
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))

@login_required
def pendingProfile(request):
    if(request.user.is_staff):
        profiles = Profile.objects.filter(verified = False)
        diction = {'title':'Pending Profiles','profiles':profiles}
        return render(request,'Staff/pendingProfile.html',context=diction)
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))

@login_required
def updateProfile(request,pk):
    
    if(request.user.is_staff):
        updateOption = True
        profile = Profile.objects.get(pk=pk)
        profile_form = ProfileUpdateForm(instance=profile)
        if request.method == 'POST':
            profile_form = ProfileUpdateForm(instance=profile,data=request.POST)
            if profile_form.is_valid():
                profile_form.save()
                if profile.userType==1:
                    return HttpResponseRedirect(reverse('appStaff:viewDonors'))
                else:
                    return HttpResponseRedirect(reverse('appStaff:viewVolunteer'))
        diction = {'title':'Profile Update Form','profile_form':profile_form,'update':updateOption}
        # return render(request,'Staff/profileUpdate.html',context=diction)
        return render(request,'Staff/pendingProfile.html',context=diction)
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))

@login_required
def deleteProfile(request,pk):
    if(request.user.is_staff):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return render(request,'Staff/pendingProfile.html')
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))
@login_required
def viewDonors(request):
    if(request.user.is_staff):
        profiles = Profile.objects.filter(userType=1,verified = True)
        diction = {'title':'List of Donors','profiles':profiles}
        return render(request,'Staff/pendingProfile.html',context=diction)
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))

@login_required
def viewVolunteer(request):
    if(request.user.is_staff):
        profiles = Profile.objects.filter(userType=2,verified = True)
        diction = {'title':'List of Volunteers','profiles':profiles}
        return render(request,'Staff/pendingProfile.html',context=diction)
    else:
        return HttpResponseRedirect(reverse('accounts:userProfile'))