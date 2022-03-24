
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Accounts.forms import UserForm,ProfileForm,ProfileUpdateForm
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
            return HttpResponse("Account Created SuccessFully")
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
            return userProfile(request)
    return render(request,'Accounts/userUpdate.html',context = {'profile_form':profile_form})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                #this changed url also
                # return HttpResponse("Login SuccessFull")
                #This two doesnot change url
                # return render(request,'index.html',context={})
                return userProfile(request)

            else:
                return HttpResponse("User is not Active")
        else:
            return HttpResponse("Login details are wrong")
    else:
        return render(request,'Accounts/login.html',context={})
    
@login_required
def userLogout(request):
    logout(request)
    return home(request)

@login_required
def userProfile(request):
    return render(request,'accounts/profile.html')