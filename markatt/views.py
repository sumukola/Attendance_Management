from django.shortcuts import redirect, render
from django.db import connection
from .forms import Attform
# Create your views here.
def mark(request,tablename):
    students = get_students(request,tablename)
    form = Attform().as_p
    return render(request,'mark.html',{'students':students,'form':form,'classname':tablename})

def get_att(request,classname):
    d={}
    try:
        s=list(request.POST.items())
        flag1 = 0
        flag2 = 0 
        for i in s:
            if flag1==0:
                flag1=1
            elif flag2==0:
                flag2=1
                date = i[1]
            else:
                d[i[0][1:2]] = i[1]
    except:
        pass
    return render(request,'sample.html',{'status':(date,d,classname)})

def get_students(request,classname):
    with connection.cursor() as cursor:
        cursor.execute("select * from {}".format(classname))
        students = cursor.fetchall()
    return students