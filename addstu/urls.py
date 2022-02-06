from django.urls import path
from addstu import views 
urlpatterns = [
    path('addordel/<classname>',views.addordel,name='addordel'),
    path('stu_cred/<classname>',views.stu_cred,name='stu_cred')
]