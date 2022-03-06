from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import stu_form
from django.db import connection

# Create your views here.
def addordel(request,classname):
    form = stu_form()
    content = class_content(classname)
    return render(request,'add_students.html',{'forms':form,'classname':classname,'students':content})

def stu_cred(request,classname):
    if request.method == "POST":
        rollno , usn , name = stu_form(request.POST)
        rollno = rollno.value()
        usn = usn.value()
        name = name.value()
    with connection.cursor() as cursor:
        query = "insert into {0} values({1},'{2}','{3}')".format(classname,rollno,usn,name)
        cursor.execute(query)
    return redirect('addordel',classname)
    
def class_content(classname):
    with connection.cursor() as cursor:
        cursor.execute("select * from {};".format(classname))
        content = cursor.fetchall()
    return content
