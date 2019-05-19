from django.shortcuts import *
from django.http import *
from .models import *
from django.template import *

# Create your views here.

def to_index(request):
    return redirect('index')

def index(request):
    response = render_to_response('miseem_index.html')
    return response

def example(request, current):
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
        if current == 1:
            form = PointWise(request.POST)
        elif current == 2:
            form = PairWise(request.POST)
        elif current == 3:
            form = ListWise(request.POST)
        else:
            return render(request, 'sorry.html')
        response = HttpResponse("test!")

    else:
        raise Http404("The page doesn't exist!")
    return response

def quiz(request):
    response = render(request, 'quiz.html')
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
