from rest_framework import viewsets
from .models.models import Bus, Schedule, Passager, Reservation, Route
from .serializer import BusSerializer, ScheduleSerializer, PassagerSerializer, ReservationSerializer, RouteSerializer
from api.permissions import ProductsAccessPermissions

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie



class PassagerViewset(viewsets.ModelViewSet):
    queryset = Passager.objects.all()
    serializer_class = PassagerSerializer

class BusViewset(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class RouteViewset(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ScheduleViewset(viewsets.ModelViewSet):
    # queryset = Departure.objects.all()
    queryset = Schedule.objects.select_related().all()
    serializer_class = ScheduleSerializer
    filterset_fields = ['date_of_travel', 'route__from_destination','route__to_destination']

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super(ScheduleViewset, self).dispatch(*args, **kwargs)


class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
