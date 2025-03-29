from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, World. You are at chai or Django home page")
    return render(request , 'websites/index.html')

def about(request):
   # return HttpResponse("Hello, World. You are at chai or Django home page")
   return render(request , 'websites/about.html')
    
def contact(request):
   # return HttpResponse("Hello, World. You are at chai or Django home page")
   return render(request , 'website/index.html')