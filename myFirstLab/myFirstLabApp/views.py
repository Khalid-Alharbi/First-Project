from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home(req):
    return HttpResponse('Hello World, This is my new HOME !')