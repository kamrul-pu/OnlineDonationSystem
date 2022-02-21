from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    diction = {'title':'Homepage'}
    return render(request,'Accounts/index.html',context=diction)
