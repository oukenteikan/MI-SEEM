from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def to_home(request):
    return HttpResponseRedirect('index')

def home(request):
    return HttpResponse("I'm trying to build an econcs website for our group!")
