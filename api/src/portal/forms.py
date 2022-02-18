from django.forms import ModelForm
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
    