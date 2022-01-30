from django.shortcuts import render
from django.views.generic import ListView
from .forms import stu_form

# Create your views here.
def addordel(request):
    form = stu_form()
    return render(request,'add_students.html',{'forms':form})

def stu_cred(request):
    if request.method == "POST":
        rollno , usn , name = stu_form(request.POST)
        
