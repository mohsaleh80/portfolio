
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('', views.Home),
    path('home/', views.Home),
    path('profile/', views.About),
    path('about/', views.About),
    path('contact/', views.Contact),
    
]