from django.urls import path, include
from JathnielApp import views

urlpatterns = [
    path('', views.landingPage, name="landing"),
    path('home/', views.homePage, name="home"),
    path('index/', views.indexPage, name="index"),
    path('contact/', views.contactPage, name="contact"),
    path('about/', views.aboutPage, name="about"),
    path('subscription/', views.subscriptionPage, name="subscription"),
    path('activities/', views.activitiesPage, name="activities"),
    path('success/', views.successPage, name="success"),
]
