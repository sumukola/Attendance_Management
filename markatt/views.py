from django.shortcuts import render
from django.db import connection
from .forms import Attform
# Create your views here.
def mark(request,tablename):
    students = get_students(request,tablename)
    form = Attform()
    return render(request,'mark.html',{'students':students,'form':form})

def get_students(request,classname):
    with connection.cursor() as cursor:
        cursor.execute("select * from {}".format(classname))
        students = cursor.fetchall()
    return students