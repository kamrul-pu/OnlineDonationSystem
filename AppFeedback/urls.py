from django.urls import path
from AppFeedback import views
app_name="appFeedback"

urlpatterns = [
    path('',views.feedback,name='feedback'),
    path('like/<int:pk>/',views.likeFeedback,name='like'),
]