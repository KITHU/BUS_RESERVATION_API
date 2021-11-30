from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import FilesViewset, ProductsViewset

router = routers.DefaultRouter()

router.register(r'product', ProductsViewset)
router.register(r'file', FilesViewset)

urlpatterns = [
    path('', include(router.urls)),
]
