from django.urls import path
from AppDonation import views
app_name="appDonation"

urlpatterns = [
    path('',views.Dontaion,name='donation'),
]