
from django.http   import HttpResponse


def Home(request):
    data = "This is Home Admin Page..."
    return HttpResponse(data)

def About(request):
    data = "This is About Admin Page..."
    return HttpResponse(data)

def Contact(request):
    data= "This is Contact Admin Page..."
    return HttpResponse(data)