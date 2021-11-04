from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import ProductsViewset

router = routers.DefaultRouter()

router.register(r'product', ProductsViewset)

urlpatterns = [
    path('', include(router.urls)),
]
