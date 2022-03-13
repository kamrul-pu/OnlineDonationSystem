from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    diction = {'title':'Homepage'}
    return render(request,'home.html',context=diction)
