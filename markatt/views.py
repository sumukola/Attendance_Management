from django.shortcuts import redirect, render
from django.db import connection
from .forms import Attform
import re 
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
                roll_number = re.findall('[0-9]+',i[0])
                d[roll_number[0]] = i[1]
        table_cols = write_to_db(request,date,classname,d)
        return redirect(mark,classname)
    except:
        return render(request,'mark.html',{'status':"Something went wrong while marking attendance. Please make sure you did it correctly."})
    
def write_to_db(request,date,classname,d):
    date = date[5:7] + date[8:] + date[:4]
    with connection.cursor() as cursor:
        tables_cols = cursor.execute("PRAGMA table_info({})".format(classname))
        columns = [i[1] for i in tables_cols]
        if 'd'+date not in columns:
            cursor.execute("alter table {} add d{} varchar".format(str(classname),str(date))) 
            for rollno,status in d.items():
                cursor.execute("update {0} set d{1} = '{2}' where rollno={3}".format(classname,date,status,rollno))
        else:
            mark(request,classname)   
    return 

def get_students(request,classname):
    with connection.cursor() as cursor:
        cursor.execute("select rollno,usn,name from {}".format(classname))
        students = cursor.fetchall()
    return students