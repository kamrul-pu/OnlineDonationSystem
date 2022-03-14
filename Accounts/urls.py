from django.urls import path
from Accounts import views
app_name= 'accounts'

urlpatterns = [
    path('user_login/',views.userLogin,name='userLogin'),
    path('user_logout/',views.userLogout,name="userLogout"),
    path('user_profile/',views.userProfile,name="userProfile"),
    path('register/',views.RegisterUser,name='registerUser'),
    path('user_update/<pk>/',views.UserUpdate,name='updateProfile'),
]