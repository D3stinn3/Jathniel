from django.urls import path, include
from JathnielApp import views

urlpatterns = [
    path('home/', views.homePage, name="home"),
    path('index/', views.indexPage, name="index"),
]
