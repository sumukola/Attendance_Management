from django.urls import path
from class_creation import views

urlpatterns = [
    path('createclass',views.show_class_details_page,name="createclass"),
    path('take_class_vals',views.take_class_vals,name="take_class_vals"),
]