from django.urls import path
from Accounts import views
app_name= 'accounts'

urlpatterns = [
    path('signup_donar/',views.signupDonar,name='signupDonar'),
    path('signup_volunteer/',views.signupVolunteer,name='signupVolunteer'),
    path('user_login/',views.userLogin,name='userLogin'),
    path('user_logout/',views.userLogout,name="userLogout"),
]