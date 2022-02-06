from random import sample
from typing import Collection
from django.shortcuts import redirect, render 
from django.db import connection, connections
from django.contrib import messages
from class_creation import views

def get_username(request):
    return request.user.username

def home(request):
    username = get_username(request)
    tables = connection.introspection.table_names()
    usertables = []
    for table in tables:
        if table.startswith(username):
            usertables.append(table)
    if len(usertables)!=0:
        return render(request,'homepage.html',{'tables':usertables})
    return render(request,'homepage.html',{"messages":['Classes created are displayed here.']})

def createclass(request):
    return render(request,'class_creation/views/show_class_details_page')

def delete_class(request,tablename):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute('Drop table {}'.format(tablename))
    return redirect('homepage')

def show_class(request,classname):
    with connection.cursor() as cursor:
        cursor.execute("select * from {}".format(classname))
        students = cursor.fetchall()
    return render(request,'show_class.html',{'students':students})