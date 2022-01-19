from django.urls import path , include 
from . import views 
urlpatterns = [path('',views.home),
    path('homepage',views.home,name="homepage"),
    path('',include('class_creation.urls'))
]
