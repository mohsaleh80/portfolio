from django.shortcuts import render
from django.http   import HttpResponse
# Create your views here.


def Home(request):
    #data = "This is Employee Home Admin Page..."
    #return HttpResponse(data)
    return render(request,'employee/index.html')
    

def Profile(request):
   # data = "This is Employee Profile Admin Page..."
   # return HttpResponse(data)
    return render(request,'employee/profile.html')

def About(request):
    #data = "This is Employee About Admin Page..."
    #return HttpResponse(data)
    return render(request,'employee/about.html')

def Contact(request):
    # data= "This is Employee Contact Admin Page..."
    #return HttpResponse(data)
    return render(request,'employee/contact.html')
