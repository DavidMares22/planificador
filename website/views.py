from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import MyAuthForm,MyregForm
from django.db import IntegrityError




# Create your views here.


def welcome(request):
    context = {'meetings': Meeting.objects.all()}
    return render(request,'website/home.html',context)

def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))

def loginuser(request):
    form = MyAuthForm()
    if request.method == "POST":
        form = MyAuthForm(data=request.POST)    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                    
                    do_login(request, user)
                    
                    return redirect('home')            
    return render(request,'website/login.html', {'form': form})


def logoutuser(request):
    do_logout(request)
    return redirect('home')


def registeruser(request):
    if request.method == 'POST':
        form = MyregForm(request.POST)
        if form.is_valid():
            user = User()
            user.save()
            if user is not None:
                
                do_login(request, user)
                
                return redirect('home')            

    else:
        form = MyregForm()
    return render(request, 'website/register.html', {'form': form})

