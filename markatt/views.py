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
        write_to_db(request,date,classname,d)
        return render(request,'sample.html',{'status':date})
    except:
        return render(request,'mark.html',{'status':"Something went wrong while marking attendance. Please make sure you did it correctly."})
    
def write_to_db(request,date,classname,d):
    date = date[5:7] + date[8:] + date[:4]
    with connection.cursor() as cursor:
        cursor.execute("alter table {} add d{} varchar".format(str(classname),str(date)))
        for rollno,status in d.items():
            cursor.execute("update {} set d{} = '{}' where rollno={}".format(classname,date,status,rollno))
    return

def get_students(request,classname):
    with connection.cursor() as cursor:
        cursor.execute("select rollno,usn,name from {}".format(classname))
        students = cursor.fetchall()
    return students