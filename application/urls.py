from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_application, name='application'),
    path('succes', views.succes, name='succes')
    ]