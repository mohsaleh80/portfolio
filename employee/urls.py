
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.Home,name="employee.home"),
    path('home/', views.Home,name="employee.home"),
    path('profile/', views.Profile,name="employee.profile"),
    path('about/', views.About,name="employee.about"),
    path('contact/', views.Contact,name="employee.contact"),
    
]