from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.


def welcome(request):
    context = {'meetings': Meeting.objects.all()}
    return render(request,'website/home.html',context)

def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))