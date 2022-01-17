from django.urls import path , include 
from . import views 
urlpatterns = [path('',views.home),
    path('createclass/',include('class_creation.urls'))]
