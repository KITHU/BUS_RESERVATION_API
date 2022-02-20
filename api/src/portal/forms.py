from django.forms import ModelForm
from django import forms
from api.src.tickets.models.models import Bus, Route, Schedule



class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_name', 'no_of_seat']


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ['from_destination', 'to_destination']


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
           'departure_time':forms.DateInput(attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'time'
              }),
            'arrival_time':forms.DateInput(attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'time'
              }),
            'date_of_travel': forms.DateInput(
             format=('%Y-%m-%d'),
              attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
        }
