from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.register,name='register'),
    path('register/',views.register),
    path('login_user/',views.login_user,name='login_user'),
]