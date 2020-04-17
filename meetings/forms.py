from django import forms
from .models import Meeting,Room
from datetime import date
from django.core.exceptions import ValidationError


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

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError('Meetings can not be in the past')
        return d

       