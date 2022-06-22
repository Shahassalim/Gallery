from django.urls import path
from media_app import views

urlpatterns=[
    path('',views.Display,name="Display")
   
]