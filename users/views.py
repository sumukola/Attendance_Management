from cmath import log
from contextlib import redirect_stderr
from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# Create your views here.

def register(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            Username = request.POST['username']
            Password = request.POST['password1']
            user = authenticate(request,username=Username,password=Password)
            login(request,user)
            return render(request,'homepage.html')
    else:
        forms = UserCreationForm()
    return render(request,'user_register.html',{'form':forms})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'homepage.html')
        else:
            messages.success(request,'Incorrect Username or Password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    forms = UserCreationForm()
    return render(request,'user_register.html',{'form':forms})