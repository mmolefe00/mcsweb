from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# Home Page View
def index(request):
    return render(request, 'index.html', {'nbar': 'home'})

def about(request):
    return render(request, 'about.html', {'nbar': 'about'})

def philosophy(request):
    return render(request, 'philosophy.html', {'nbar': 'philosophy'})

def services(request):
    return render(request, 'services.html', {'nbar': 'services'})

def contact(request):
    return render(request, 'contact.html', {'nbar': 'contact'})
