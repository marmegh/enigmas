from django import forms
from django.forms import extras

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255)
    pwd = forms.CharField(label='Password', max_length=255, widget = forms.PasswordInput)
class RegistrationForm(forms.Form):
    name = forms.CharField(label="Name", max_length = 255, widget = forms.TextInput)
    username = forms.CharField(label="Username", max_length = 255, widget = forms.TextInput)
    email = forms.CharField(label='Email', max_length=255, widget = forms.EmailInput)
    pwd = forms.CharField(label='Password', max_length=255, widget = forms.PasswordInput)
    cpw = forms.CharField(label='Confirm Password', max_length=255, widget = forms.PasswordInput)
