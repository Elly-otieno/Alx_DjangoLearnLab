from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# FUNCTION BASED VIEWS

def hello_view(request):
    '''A basic function view returning a greeting message.'''
    return HttpResponse('Hello, World!')

