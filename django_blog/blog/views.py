from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    """
    return to Home page
    """
    return HttpResponse('<h1> You are in Home Page </h1>')

def about(request):
    """
    return to About Page
    """
    return HttpResponse('<h1> You are in About Page </h1>')
