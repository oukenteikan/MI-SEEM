from django.shortcuts import *
from django.http import *
from .models import *

# Create your views here.

def to_index(request):
    return redirect('index')

def index(request):
    response = render_to_response('miseem_index.html')
    return response

def example(request, current):
    context = {}
    context['current'] = current
    if current == 1:
        context['head'] = "The 1st example!"
    elif current == 2:
        context['head'] = "The 2nd example!"
    elif current == 3:
        context['head'] = "The 3rd example!"
    else:
        raise Http404("The page doesn't exist!")
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
