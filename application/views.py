from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicationForm

# Create your views here.

def succes(request):
    return render(request, 'application/succes.html')

def create_application(request):
    error = ''
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
        else:
            error = 'Неверный номер телефона'
    form = ApplicationForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'application/application.html', context=data)