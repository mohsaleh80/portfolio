from django.shortcuts import render
from django.http   import HttpResponse
# Create your views here.


def Home(request):
    data = "This is Employee Home Admin Page..."
    return HttpResponse(data)

def Profile(request):
    data = "This is Employee Profile Admin Page..."
    return HttpResponse(data)

def About(request):
    data = "This is Employee About Admin Page..."
    return HttpResponse(data)

def Contact(request):
    data= "This is Employee Contact Admin Page..."
    return HttpResponse(data)
