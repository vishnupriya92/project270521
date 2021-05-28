from django.urls import path
from myapp31 import views

app_name="myapp31"

urlpatterns=[
    path('',views.index,name="index"),
    path('con/',views.details,name="con"),
    path('menu/',views.menu,name="menu"),
]