from django.shortcuts import render
from .models import Meeting
# Create your views here.


def detail(request,id):
    meeting = Meeting.objects.get(pk=id)
    context = {'meeting':meeting}
    return render(request,'meetings/detail.html',context)