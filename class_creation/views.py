from email import message
from django.shortcuts import render
from .forms import Sem , Sec , Sub
from django.db import connection
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def show_class_details_page(request):
    form1 = Sem()
    form2 = Sec()
    form3 = Sub()
    return render(request, 'classdetails.html', {'form1':form1,'form2':form2,'form3':form3})

def createtable(classname):
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE {} (rollno INTEGER NOT NULL PRIMARY KEY,usn TEXT NOT NULL UNIQUE,name TEXT NOT NULL)".format(classname))
    return 

def take_class_vals(request):
    if request.method == "POST":
        form1= Sem(request.POST)
        form2= Sec(request.POST)
        form3 = Sub(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            sem = form1.cleaned_data.get("SEMS")
            sec = form2.cleaned_data.get("SEC")
            sub = form3.cleaned_data.get('SUB')
        else:
            form1 = Sem()
            form2 = Sec()
            form3 = Sub()
            return render(request,'classdetails.html',{'form1':form1,'form2':form2,'form3':form3})
        username = 'sumanth'
        classname = str(sec) +str(sem) + str(sub)
        if classname not in connection.introspection.table_names():
            createtable(classname)
        else:
            form1 = Sem()
            form2 = Sec()
            form3 = Sub()
            message = messages.success(request,'This class already exists!!Create different one.')
            return render(request,'classdetails.html',{'form1':form1,'form2':form2,'form3':form3})
        return render(request,'homepage.html',{'username':username})