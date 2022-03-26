from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    feedbackTopic = models.CharField(max_length=50,blank=True,null=True)
    feedback = models.TextField(max_length=200)
    feedbackDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-feedbackDate',)
    
    def __str__(self):
        return f"{self.user} {self.feedback}"

class Likes(models.Model):
    feedback = models.ForeignKey(Feedback,on_delete=models.CASCADE,related_name='like_feedback')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    def __str__(self):
        return f"{self.user} {self.feedback}"