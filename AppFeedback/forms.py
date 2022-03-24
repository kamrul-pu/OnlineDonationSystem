from django import forms
from AppFeedback.models import Feedback,Likes
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback',)

class LikesForm(forms.ModelForm):
    class Meta:
        model = Likes
        fields = "__all__"