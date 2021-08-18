from typing import Set
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Post
from django.conf import settings
# Create your views here.

def home(request):
    if request.POST:
        username=request.POST.get('username')
        text=request.POST.get('textpost')
        user=User.objects.filter(username=username).first()
        if user is not None:
            user_obj=Post(username=user,Message=text)
            user_obj.save()
            messages.success(request, 'post Created')
        else:
            messages.success(request, 'username no fount')
            return redirect(request,'/home')
    return render(request,'Createpost.html')
  
def index(request):
    return render(request, "index.html")
def login(request):
    if request.POST:
        username=request.POST.get('username')
        passward=request.POST.get('passward')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'user is not found')
            return redirect('/login') 
        user=authenticate(request,username=username,password=passward)
        if user is not None:
             auth_login(request,user)
             return redirect('/home')
            
        else:
             messages.success(request, 'wrong password')
             return HttpResponse(user)  
            
    return render(request,"login.html")

def register(request):
    if request.POST:
        username=request.POST.get("username")
        Email=request.POST.get('email')
        Firstname=request.POST.get('Firstname')
        Lastname=request.POST.get('Lastname')
       
        Passward=request.POST.get('password') 
        
        if User.objects.filter(username=username).first():
            messages.success(request, 'username is already taken.')
            return redirect('/register')
        if User.objects.filter(email=Email).first():
            messages.success(request, 'email is already taken.')
            return redirect('/register')
        user_obj=User(username=username,email=Email,first_name=Firstname,last_name=Lastname)
        user_obj.set_password(Passward)
        user_obj.save()
        messages.success(request, 'User Register Sucessfully! Go to login')
    return render(request,"register.html")       