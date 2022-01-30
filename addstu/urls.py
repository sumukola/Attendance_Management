from django.urls import path
from addstu import views 
urlpatterns = [
    path('addordel',views.addordel,name='addordel'),
    path('stu_cred',views.stu_cred,name='stu_cred')
]