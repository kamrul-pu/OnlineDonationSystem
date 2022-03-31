from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from AppFeedback.forms import FeedbackForm
from AppFeedback.models import Feedback,Likes

# Create your views here.

@login_required
def feedback(request):
    feedbacks = Feedback.objects.all()
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return HttpResponseRedirect(reverse('appFeedback:feedback'))
    feedback_form = FeedbackForm()
    diction = {'title':'User Feedback','feedback_form':feedback_form,'feedbacks':feedbacks}
    return render(request,'Feedback/feedback.html',context = diction)

@login_required
def likeFeedback(request,pk):
    feedback = Feedback.objects.get(pk=pk)
    already_liked = Likes.objects.filter(feedback=feedback,user=request.user)
    if not already_liked:
        liked_post = Likes(feedback=feedback,user=request.user)
        liked_post.save()
    else:
        already_liked.delete()
    return HttpResponseRedirect(reverse('appFeedback:feedback'))
    # return HttpResponse("Liked")

@login_required
def unlikeFeedback(request,pk):
    feedback = Feedback.objects.get(pk=pk)
    already_liked = Likes.objects.filter(feedback=feedback,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('appFeedback:feedback'))