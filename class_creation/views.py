from email import message
from django.shortcuts import redirect, render
from .forms import Sem , Sec , Sub
from django.db import connection
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import connection

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

def sample_view(request):
    return request.user.username

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
        username = sample_view(request)
        classname = username + '_' + str(sec) +str(sem) + str(sub)
        cname =  str(sec) +str(sem) + str(sub)
        if check(cname):
            createtable(classname)
            usertables = usertab(username)
            return redirect('homepage')
        else:
            form1 = Sem()
            form2 = Sec()
            form3 = Sub()
            return render(request,'classdetails.html',{'form1':form1,'form2':form2,'form3':form3,'messages':['This class is already taken. Create different one.']})
        

def check(classname):
    tables = connection.introspection.table_names()
    for table in tables:
        if table.endswith(classname):
            return False 
    return True

def usertab(username):
    tables = connection.introspection.table_names()
    usertables = []
    for table in tables:
        if table.startswith(username):
            usertables.append(table)
    return usertables