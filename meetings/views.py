from django.shortcuts import render, get_object_or_404,redirect
from .models import Meeting,Room
from .forms import MeetingForm
# Create your views here.


def detail(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    context = {'meeting':meeting}
    return render(request,'meetings/detail.html',context)


def room(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'meetings/rooms.html',context)


def new(request):
    if request.method == 'POST':
        
        form = MeetingForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('home')
            
    else:
        form = MeetingForm()

    return render(request,'meetings/new.html',{'form':form})