from django import views
from django.urls import path 
from . import views
urlpatterns = [
    path('markatt/<tablename>',views.mark,name='markatt')
]