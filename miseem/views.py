from django.shortcuts import *
from django.http import *
from .models import *

# Create your views here.

def to_index(request):
    return redirect('index')

def index(request):
    response = render_to_response('index.html')
    return response

def example(request, current):
    context = {}
    context['current'] = current
    response = render_to_response('example.html', context)
    return response

def quiz(request):
    response = render_to_response('quiz.html')
    return response

def entry(request):
    response = render_to_response('entry.html')
    return response

def task(request):
    response = render_to_response('task.html')
    return response

def sorry(request):
    response = render_to_response('sorry.html')
    return response

def thanks(request):
    response = render_to_response('thanks.html')
    return response
