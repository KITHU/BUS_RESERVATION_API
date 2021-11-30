from rest_framework import viewsets
from .models.models import Files, Products
from .serializer import FilesSerializer, ProductSerializer
from api.permissions import ProductsAccessPermissions



class ProductsViewset(viewsets.ModelViewSet):
    permission_classes = [ProductsAccessPermissions]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class FilesViewset(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
