from django.db import models
from django.contrib.auth.models import User
from Accounts.models import District
# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30,blank=False,null=False)

    def __str__(self):
        return f"{self.cname}"

class Donations(models.Model):
    donationCategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='donations')
    district = models.ForeignKey(District,on_delete=models.CASCADE,related_name='district')
    productName = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(max_length=200)
    choise = (
        ("Pending",'Pending'),
        ("Delivered",'Delivered'),
        ("Distributed",'Distributed'),
    )
    status = models.CharField(choices=choise,max_length=15)
    distributed = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user} {self.donationCategory}: {self.productName}"
