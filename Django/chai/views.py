from django.shortcuts import render

# Create your views here.

def all_chai(request):
    return render(request, 'chai/all_chai.html')

def home(request):
    return render(request, 'chai/index.html')