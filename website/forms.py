from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,User
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class MyAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'user'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))


class MyregForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'user'}),label='User')
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),label='Password')
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Repeat password'}),label='Repeat password')

    # class Meta:
    #     model=User
    #     fields = ['username','password1','password2']

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     return password2
            