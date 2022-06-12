from django.urls import path, re_path
from addstu import views 


urlpatterns = [
    path('add_students/<classname>',views.add_students,name='add_students'),
    path('stu_cred/<classname>',views.stu_cred,name='stu_cred'),
    path('delete_students/<classname>',views.delete_students,name="delete_students"),
    path('delete/<classname>',views.delete,name="delete")
]