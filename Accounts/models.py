from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Division(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class Profile(models.Model):

    profile = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    uType = (
        (1,'Donor'),
        (2,'Volunteer'),
    )
    userType = models.IntegerField(choices=uType)
    phoneNo = models.CharField(max_length=15)
    nationalId = models.CharField(max_length=20)
    divison = models.ForeignKey(Division,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to = 'profile',blank=True)
    verified = models.BooleanField(default=False)
    signupTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} {self.district}"
