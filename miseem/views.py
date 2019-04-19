from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def to_index(request):
    return HttpResponseRedirect('index')

def index(request):
    response = render(request, 'index.html')
    return response

def example(request, current):
    context = {}
    context['current'] = current
    context['next'] = 'example' + str(current + 1)
    response = render(request, 'example.html', context)
    return response

def quiz(request):
    response = render(request, 'quiz.html')
    return response

def entry(request):
    response = render(request, 'entry.html')
    return response

def task(request):
    response = render(request, 'task.html')
    return response

def sorry(request):
    response = render(request, 'sorry.html')
    return response

def thanks(request):
    response = render(request, 'thanks.html')
    return response