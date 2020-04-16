from django import forms
from .models import Meeting,Room
from django.forms.fields import MultipleChoiceField

class MeetingForm(forms.ModelForm):
   
    class Meta:
        model = Meeting
        fields = ['title','date','start_time','duration','room']    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
        }

       