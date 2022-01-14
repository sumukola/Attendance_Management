from django.urls import path
from class_creation import views

urlpatterns = [
    path('',views.show_class_details_page),
]