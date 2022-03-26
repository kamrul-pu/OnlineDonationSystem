from django.urls import path
from . import views
app_name = 'appVolunteer'

urlpatterns = [
    path('viewDonor/',views.viewDonors,name='viewDonors'),
    path('view-Donations/<pk>/',views.viewDonations,name='viewDonations'),
]