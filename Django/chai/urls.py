from django.contrib import admin
from django.urls import path
from . import views

#localhost:8000/chai
urlpatterns = [
    path('all_chai/', views.all_chai, name='all_chai'),
    path('', views.home, name='home'),
   
]