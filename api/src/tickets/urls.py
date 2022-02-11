from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import BusViewset, DepartureViewset, PassagerViewset, ReservationViewset, RouteViewset

router = routers.DefaultRouter()

router.register(r'passager', PassagerViewset)
router.register(r'bus', BusViewset)
router.register(r'route', RouteViewset)
router.register(r'departure', DepartureViewset)
router.register(r'reservation', ReservationViewset)

urlpatterns = [
    path('', include(router.urls)),
]
