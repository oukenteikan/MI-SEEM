from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return HttpResponse("I'm trying to build an econcs website for our group!")
