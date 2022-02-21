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

class Donor(models.Model):
    donor = models.OneToOneField(User,on_delete=models.CASCADE,related_name='donar')
    # Name = models.CharField(max_length=100)
    # lastName = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=15)

    nationalId = models.CharField(max_length=20)
    areas = (
        (1,'Dhaka'),
        (2,'Chittagong'),
        (3,'Rajshahi'),
        (4,'Barishal'),
        (5,'Khulna'),
        (6,'Mymenshing'),
        (7,'Rangpur'),
        (8,'Sylhet'),
    )
    # donarDivision = models.IntegerField(choices=areas)
    donorDivision = models.ForeignKey(Division,on_delete=models.CASCADE)
    donorDistrict = models.ForeignKey(District,on_delete=models.CASCADE)
    donorAddress = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to = 'donor',blank=True)
    isDonor = models.BooleanField(default=False)
    signupTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.donor} {self.donorDistrict}"

class Volunteer(models.Model):
    volunteer = models.OneToOneField(User,on_delete=models.CASCADE,related_name='volunteer')
    # Name = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=15)
    nationalId = models.CharField(max_length=20)
    areas = (
        (1,'Dhaka'),
        (2,'Chittagong'),
        (3,'Rajshahi'),
        (4,'Barishal'),
        (5,'Khulna'),
        (6,'Mymenshing'),
        (7,'Rangpur'),
        (8,'Sylhet'),
    )
    # volunteerDivison = models.IntegerField(choices=areas)
    volunteerDivison = models.ForeignKey(Division,on_delete=models.CASCADE)
    volunteerDistrict = models.ForeignKey(District,on_delete=models.CASCADE)
    volunteerAddress = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to = 'volunteer',blank=True)
    isVolunteer = models.BooleanField(default=False)
    signupTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.volunteer} {self.volunteerDistrict}"
