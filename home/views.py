from random import sample
from typing import Collection
from django.shortcuts import render 
from django.db import connection, connections
from django.contrib import messages
from class_creation import views

def sample_view(request):
    return request.user.username

def home(request):
    username = sample_view(request)
    tables = connection.introspection.table_names()
    usertables = []
    for table in tables:
        if table.startswith(username):
            usertables.append(table)
    if len(usertables)!=0:
        return render(request,'homepage.html',{'tables':usertables})
    else:
        message = messages.success(request,"You didn't create any class")
        return render(request,'homepage.html',{'message':message})

def createclass(request):
    return render(request,'class_creation/views/show_class_details_page')

def delete_class(request,tablename):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute('Drop table {}'.format(tablename))
        usertables = views.usertab(username)
    return render(request,'homepage.html',{'tables':usertables})