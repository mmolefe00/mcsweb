from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# Home Page View
def greeting(request):
    return HttpResponse('Welcome to the MCS Homepage!')

def about(request):
    return HttpResponse('About Us:')

def philosophy(request):
    return HttpResponse('Our Philosophy:')

def services(request):
    return HttpResponse('Our Services:')

def contact(request):
    return HttpResponse('Contact Us:')
