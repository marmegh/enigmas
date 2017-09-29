from django import forms
from django.forms import extras

class NewTripForm(forms.Form):
    destination = forms.CharField(label='Destination', max_length=255)
    plan = forms.CharField(label = 'Description')
    start = forms.DateField(label = 'Travel Date From', widget = extras.SelectDateWidget(years = range(2017,2050)))
    start = forms.DateField(label = 'Travel Date To', widget = extras.SelectDateWidget(years = range(2017,2050)))
