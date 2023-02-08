
from django.shortcuts import render
from django.http   import HttpResponse


def Home(request):
    data = {"Slogan":"This is Home Admin Page...",
            "Services":["Web","Desktop","Mobile","Hosting"]
            }  
   # return HttpResponse(data)
    return render(request,'index.html',data)

def About(request):
    data = {"Slogan":"This is About Admin Page..."}  
    #return HttpResponse(data)
    return render(request,'about.html',data)

def Contact(request):
    data = {"Slogan":"This is contact Admin Page..."}  
   # return HttpResponse(data)
    return render(request,'contact.html',data)