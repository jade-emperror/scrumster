from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('alt',views.alt,name="alt"),
    path('load',views.load,name="load")
]
