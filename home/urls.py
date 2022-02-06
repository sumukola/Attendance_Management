from django.urls import path , include 
from . import views 
urlpatterns = [path('',views.home),
    path('homepage',views.home,name="homepage"),
    path('',include('class_creation.urls')),
    path('delete_class/<tablename>',views.delete_class,name="delete_class"),
    path('show_class/<classname>',views.show_class,name='show_class')
]
