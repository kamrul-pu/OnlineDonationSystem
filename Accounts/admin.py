from django.contrib import admin
from Accounts.models import Donor,Volunteer,District,Division
# Register your models here.

admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(District)
admin.site.register(Division)