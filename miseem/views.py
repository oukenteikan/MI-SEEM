from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *
from django.template import *
from datetime import datetime

# Create your views here.

def to_index(request):
    return redirect('miseem:index')

def index(request):
    response = render(request, 'miseem_index.html')
    return response

def example(request, current):
    if request.COOKIES.get("visited_example"+str(current)):
        return render(request, 'sorry.html')
    if request.method == "GET":
        context = {}
        context['current'] = current
        if current == 1:
            context['head'] = "The 1st example!"
            context['form'] = PointWise()
        elif current == 2:
            context['head'] = "The 2nd example!"
            context['form'] = PairWise()
        elif current == 3:
            context['head'] = "The 3rd example!"
            context['form'] = ListWise()
        else:
            return render(request, 'sorry.html')
        response = render(request, 'example.html', context)
    
    elif request.method == "POST":
        context = {}
        context['current'] = current
        if current == 1:
            context['form'] = PointWise(request.POST)
        elif current == 2:
            context['form'] = PairWise(request.POST)
        elif current == 3:
            context['form'] = ListWise(request.POST)
        else:
            return render(request, 'sorry.html')
        response = render(request, 'example.html', context)
        response.set_cookie("visited_example"+str(current), True)

    else:
        response = render(request, 'sorry.html')
    return response

def quiz(request):
    if request.COOKIES.get("visited_quiz"):
        return render(request, 'sorry.html')
    if request.method == "GET":
        context = {}
        context['form'] = Quiz()
        response = render(request, 'quiz.html', context)
    elif request.method == "POST":
        context = {}
        context['form'] = Quiz(request.POST)
        response.set_cookie("visited_quiz", True)
        response = render(request, 'quiz.html', context)
    else:
        response = render(request, 'sorry.html')
    return response

def entry(request):
    response = render(request, 'entry.html')
    return response

def task(request):
    if request.COOKIES.get("visited_task"):
        return render(request, 'sorry.html')
    response = render(request, 'task.html')
    if request.method == "POST":
        response.set_cookie("visited_task", True)
    return response

def sorry(request):
    response = render(request, 'sorry.html')
    return response

def thanks(request):
    response = render(request, 'thanks.html')
    return response
