
from django.shortcuts import render
from django.http   import HttpResponse


def Home(request):
    #data = "This is Home Admin Page..."  
   # return HttpResponse(data)
    return render(request,'index.html')

def About(request):
    #data = "This is About Admin Page..."
    #return HttpResponse(data)
    return render(request,'about.html')

def Contact(request):
   # data= "This is Contact Admin Page..."
   # return HttpResponse(data)
    return render(request,'contact.html')