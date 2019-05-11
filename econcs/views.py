from django.shortcuts import *
from django.http import *

# Create your views here.

def to_index(request):
    response = redirect('index')
    return response

def index(request):
    response = render_to_response('econcs_index.html')
    return response 
