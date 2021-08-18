from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Users import views


urlpatterns = [
    path('', views.index, name="index"),
    path('home' ,views.home,name="home"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
]