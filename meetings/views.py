from django.shortcuts import render, get_object_or_404
from .models import Meeting,Room
# Create your views here.


def detail(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    context = {'meeting':meeting}
    return render(request,'meetings/detail.html',context)


def room(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'meetings/rooms.html',context)