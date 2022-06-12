from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import stu_form
from django.db import connection
import re 

# Create your views here.
def add_students(request,classname):
    form = stu_form()
    content = class_content(classname)
    return render(request,'add_students.html',{'forms':form,'classname':classname,'students':content})

def delete_students(request,classname):
    form = stu_form()
    content = class_content(classname)
    return render(request,'delete_students.html',{'form':form,'classname':classname,'students':content})

def delete(request,classname):
    try:
        if request.method == "POST":
            students = list(request.POST)
            roll_numbers = [re.findall('[0-9]+',i) for i in students[1:]]
            roll_numbers = [i[0] for i in roll_numbers]
            cursor = connection.cursor()
            for i in roll_numbers:
                query = "delete from {} where rollno={}".format(classname,i)
                cursor.execute(query)
            return redirect('delete_students',classname)
    except:
        return render(request,'sample.html',{'classname':students})

def stu_cred(request,classname):
    if request.method == "POST":
        rollno , usn , name = stu_form(request.POST)
        rollno = rollno.value()
        usn = usn.value()
        name = name.value()
        try : 
            cursor = connection.cursor() 
            query = "insert into {0} (rollno,usn,name) values({1},'{2}','{3}')".format(classname,rollno,usn,name)
            cursor.execute(query)
        except:
            form = stu_form()
            content = class_content(classname)
            return render(request,'add_students.html',{'forms':form,'classname':classname,'students':content,'emessage':'The roll number or USN entered is already taken.'})    
        return redirect('add_students',classname)
    
def class_content(classname):
    with connection.cursor() as cursor:
        cursor.execute("select rollno,usn,name from {};".format(classname))
        content = cursor.fetchall()
    return content
