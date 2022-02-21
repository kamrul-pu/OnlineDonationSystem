from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Accounts.forms import UserForm,DonorForm,VolunteerForm
# Create your views here.

def signupDonar(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        donor_form = DonorForm(data=request.POST)
        if user_form.is_valid() and donor_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            donor_info = donor_form.save(commit=False)
            donor_info.donor = user
            if 'profile_pic' in request.FILES:
                donor_info.profile_pic = request.FILES['profile_pic']
            donor_info.save()
            registered = True
            return HttpResponse("Account Created SuccessFully")
    else:
        user_form = UserForm()
        donor_form = DonorForm()
    diction = {'title':'Donor Registration','user_form':user_form,'donor_form':donor_form,'registered':registered,'sample':'Donor Registration'}
    return render(request,'Accounts/register.html',context=diction)

def signupVolunteer(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        volunteer_form = VolunteerForm(data=request.POST)
        if user_form.is_valid() and volunteer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            volunteer_info = volunteer_form.save(commit=False)
            volunteer_info.volunteer = user
            if 'profile_pic' in request.FILES:
                volunteer_info.profile_pic = request.FILES['profile_pic']
            volunteer_info.save()
            registered = True
            return HttpResponse("Account Created SuccessFully")
    else:
        user_form = UserForm()
        volunteer_form = VolunteerForm()
    diction = {'title':'Volunteer Registration','user_form':user_form,'donor_form':volunteer_form,'registered':registered,'sample':'Volunteer Registration'}
    return render(request,'Accounts/register.html',context=diction)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                #this changed url also
                return HttpResponse("Login SuccessFull")
                #This two doesnot change url
                # return render(request,'index.html',context={})
                # return index(request)
            else:
                return HttpResponse("User is not Active")
        else:
            return HttpResponse("Login details are wrong")
    else:
        return render(request,'Accounts/login.html',context={})
    
@login_required
def userLogout(request):
    logout(request)
    return HttpResponse("logout Successfull")