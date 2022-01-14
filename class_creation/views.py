from django.shortcuts import render

# Create your views here.
def show_class_details_page(request):
    return render(request,'classdetails.html')