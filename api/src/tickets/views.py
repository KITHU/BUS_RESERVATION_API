from rest_framework import viewsets
from .models.models import Bus, Schedule, Passager, Reservation, Route
from .serializer import BusSerializer, ScheduleSerializer, PassagerSerializer, ReservationSerializer, RouteSerializer
from api.permissions import ProductsAccessPermissions



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
    filterset_fields = ['date_of_travel']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
