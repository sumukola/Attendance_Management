from django import views
from django.urls import path 
from . import views
urlpatterns = [
    path('mark/<tablename>',views.mark,name='mark'),
    path('getattendance/<classname>',views.get_att,name='getattendance')
]