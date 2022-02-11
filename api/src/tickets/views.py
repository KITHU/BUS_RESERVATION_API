from rest_framework import viewsets
from .models.models import Bus, Departure, Passager, Reservation, Route
from .serializer import BusSerializer, DepartureSerializer, PassagerSerializer, ReservationSerializer, RouteSerializer
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

class DepartureViewset(viewsets.ModelViewSet):
    # queryset = Departure.objects.all()
    queryset = Departure.objects.select_related().all()
    serializer_class = DepartureSerializer
    filterset_fields = ['date_of_travel']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
