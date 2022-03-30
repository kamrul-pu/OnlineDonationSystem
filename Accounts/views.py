from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Accounts.forms import UserForm,ProfileForm,ProfileUpdateForm
from AppDonation.models import Donations
from .models import Profile
# Create your views here.
from OnlineDonationSystem.views import home

def RegisterUser(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile_info = profile_form.save(commit=False)
            profile_info.profile = user
            if 'profile_pic' in request.FILES:
                profile_info.profile_pic = request.FILES['profile_pic']
            profile_info.save()
            registered = True
            messages.success(request,"Account Created Successfully")
            login(request,user)
            return userProfile(request)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    diction = {'title':'Donor Registration','user_form':user_form,'profile_form':profile_form,'registered':registered,'sample':'User Registration'}
    return render(request,'Accounts/register.html',context=diction)
@login_required
def UserUpdate(request,pk):
    profile = Profile.objects.get(profile=pk)
    # profile_form = ProfileForm(instance=profile)
    profile_form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(instance=profile,data=request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            if 'profile_pic' in request.FILES:
                new_profile.profile_pic = request.FILES['profile_pic']
            new_profile.save()
            return HttpResponseRedirect(reverse('accounts:userProfile'))
    return render(request,'Accounts/userUpdate.html',context = {'profile_form':profile_form})


def userLogin(request):
    msg = False
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('accounts:userProfile'))
            else:
                messages.info(request,"User is not Active")
                return HttpResponseRedirect(reverse(home))
        else:
            msg = True
            messages.error(request,"Login Details Are Wrong.Please Login Again")
            # return HttpResponseRedirect(reverse('accounts:userLogin'))
    diction = {'title':'User Login Page','msg':msg}
    return render(request,'Accounts/login.html',context=diction)
    
@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))

@login_required
def userProfile(request):
    msg1 = False
    if request.user.is_staff:
        pass
    if request.user.is_superuser:
        msg=True
        # pass
    elif request.user.profile.userType==1:
        # return HttpResponse("Donor")
        pass
    elif request.user.profile.userType==2:
        # return HttpResponse("Volunteer")
        pass
    
    diction = {'donations':'User Profile'}
    return render(request,'accounts/profile.html',context=diction)