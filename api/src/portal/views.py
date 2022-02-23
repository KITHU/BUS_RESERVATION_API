from django.forms import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from api.src.portal.filters import ScheduleFilter

from api.src.tickets.models.models import Bus, Reservation, Route, Schedule
from .forms import BusForm, RouteForm, ScheduleForm



def bus_list(request):
    buses = Bus.objects.all()
    return render(request,'bus_list.html',{'buses' : buses})


def bus_delete(request, id):
    if Bus.objects.filter(id=id):
        bus = Bus.objects.filter(id=id)
        bus.delete()
        return redirect('/api/v1/portal/bus_list/')

def bus_create(request):
    
    if request.method == 'POST':
        busform = BusForm(request.POST)
        if busform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            busform.save()
            return redirect('/api/v1/portal/bus_list')
        else:
            return redirect('/api/v1/portal/bus_create')

    else:
        busform = BusForm()
        return render(request, 'bus_create.html', {'busform': busform})



def route_list(request):
    routes = Route.objects.all()
    return render(request,'route_list.html',{'routes' : routes})


def route_delete(request, id):
    if Route.objects.filter(id=id):
        route = Route.objects.filter(id=id)
        route.delete()
        return redirect('/api/v1/portal/route_list')

def route_create(request):
    
    if request.method == 'POST':
        routeform = RouteForm(request.POST)
        if routeform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            routeform.save()
            return redirect('/api/v1/portal/route_list')
        else:
            return redirect('/api/v1/portal/route_create')

    else:
        routeform  = RouteForm()
        return render(request, 'route_create.html', {'routeform': routeform })


def schedule_create(request):
    
    if request.method == 'POST':
        scheduleform = ScheduleForm(request.POST)
        if scheduleform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            scheduleform.save()
            return redirect('/api/v1/portal/schedule_list')
        else:
            return redirect('/api/v1/portal/schedule_create')

    else:
        scheduleform = ScheduleForm()
        return render(request, 'schedule_create.html', {'scheduleform': scheduleform })


def schedule_list(request):
    schedules = Schedule.objects.all()
    myfilter = ScheduleFilter(request.GET, queryset=schedules)
    
    schedules= myfilter.qs
    
    context = {'schedules' : schedules, 'myfilter':myfilter}
    return render(request,'schedule_list.html',context)


def schedule_delete(request, id):
    if Schedule.objects.filter(id=id):
        schedule = Schedule.objects.filter(id=id)
        schedule.delete()
        return redirect('/api/v1/portal/schedule_list')


def schedule_search(request):
    schedules = Schedule.objects.all()
    

    myfilter = ScheduleFilter(request.GET, queryset=schedules)
   
    
    schedules = myfilter.qs
    
    context = {'schedules' : schedules, 'myfilter':myfilter}
  
    return render(request,'search_schedule.html',context)


def seat_seat(request):
    return render(request,'select_seat.html')