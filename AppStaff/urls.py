from django.urls import path
from AppStaff import views
app_name = 'appStaff'

urlpatterns = [
    path('',views.staff,name='staff'),
    path('pending/',views.pendingProfile,name='pendingProfile'),
    path('update/<pk>/',views.updateProfile,name='updateProfile'),
    path('delete/<pk>/',views.deleteProfile,name='deleteProfile'),
    path('viewDonors/',views.viewDonors,name='viewDonors'),
    path('viewVolunteer/',views.viewVolunteer,name='viewVolunteer'),
]