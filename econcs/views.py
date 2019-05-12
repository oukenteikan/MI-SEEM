from django.shortcuts import *
from django.http import *

# Create your views here.

def to_home(request):
    response = redirect('home')
    return response

def home(request):
    response = render_to_response('home.html')
    return response

def people(request):
    response = render_to_response('people.html')
    return response

def publication(request):
    response = render_to_response('publication.html')
    return response

def teaching(request):
    response = render_to_response('teaching.html')
    return response

def seminar(request):
    response = render_to_response('seminar.html')
    return response

def news(request):
    response = render_to_response('news.html')
    return response
