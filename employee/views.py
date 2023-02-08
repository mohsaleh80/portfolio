from django.shortcuts import render
from django.http   import HttpResponse
# Create your views here.


def Home(request):
    context = {"Slogan":"This is  Employee Home Page..."} 
    #return HttpResponse(data)
    return render(request,'employee/index.html',context)
    

def Profile(request):
    context = {"Slogan":"This is Profile Employee Page..."} 
   # return HttpResponse(data)
    return render(request,'employee/profile.html',context)

def About(request):
    context = {"Slogan":"This is About Employee  Page..."} 
    #return HttpResponse(data)
    return render(request,'employee/about.html',context)

def Contact(request):
    context = {"Slogan":"This is Employee Contact Page..."} 
    #return HttpResponse(data)
    return render(request,'employee/contact.html',context)
