from django.urls import path
from AppDonation import views
app_name="appDonation"

urlpatterns = [
    path('',views.Dontaion,name='donation'),
    path('mydonations/<pk>/',views.myDonations,name='myDonations'),
    path('updateDonation/<pk>/',views.updateDonation,name='updateDonation'),
    path('deleteDonatons/<pk>/',views.deleteDonation,name='deleteDonation'),
]