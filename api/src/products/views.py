from rest_framework import viewsets
from .models.models import Products
from .serializer import ProductSerializer
from api.permissions import ProductsAccessPermissions



class ProductsViewset(viewsets.ModelViewSet):
    permission_classes = [ProductsAccessPermissions]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
