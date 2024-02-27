from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# Home Page View
def greeting(request):
    return render(request, 'greeting.html')

def about(request):
    return render(request, 'about.html')

def philosophy(request):
    return render(request, 'philosophy.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
