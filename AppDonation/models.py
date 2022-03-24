from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30,blank=False,null=False)

    def __str__(self):
        return f"{self.cname}"

class Donations(models.Model):
    donationCategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    remarks = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.donationCategory} {self.user} {self.quantity}"
