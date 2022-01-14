from django.shortcuts import render 
def home(request):
    return render(request,'homepage.html')

def createclass(request):
    return render(request,'class_creation/views/show_class_details_page')