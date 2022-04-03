from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import feedback

# Create your views here.
def index(request):
    error = ''
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверный номер телефона'


    form = FeedbackForm()
    feedbacks = feedback.objects.all()
    data = {
        'form': form,
        'error': error,
        'feedbacks': feedbacks,
    }
    return render(request, 'homepage/index.html', context=data)