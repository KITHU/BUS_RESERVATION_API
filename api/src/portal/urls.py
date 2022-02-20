from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
     path('bus_list/', views.bus_list, name='bus_list'),
     path('bus_delete/<int:id>/',views.bus_delete, name='bus_delete'),
     path('bus_create/',views.bus_create , name='bus_create' ),

     path('route_list/', views.route_list, name='route_list'),
     path('route_delete/<int:id>/',views.route_delete, name='route_delete'),
     path('route_create/',views.route_create , name='route_create'),

     path('schedule_create/',views.schedule_create , name='schedule_create'),
     path('schedule_list/',views.schedule_list , name='schedule_list'),
     path('schedule_delete/<int:id>/',views.schedule_delete , name='schedule_delete'),

     path('schedules/',views.schedule_search , name='schedule_search'),
     path('select_seat/',views.seat_seat ,name ='select_seat'),
]