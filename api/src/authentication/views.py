from django.db.models.query import QuerySet
from rest_framework import permissions, status, generics, viewsets
from rest_framework.response import Response

from api.src.authentication.models import User

from .serializer import RegisterSerializer, LoginSerializer, UserSerializer
from api.permissions import CreateUsersPermissions, ProductsAccessPermissions

class RegisterApiView(generics.GenericAPIView):
    # permission_classes = [CreateUsersPermissions]
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiView(generics.ListAPIView):
    permissions_classes = [ProductsAccessPermissions]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_fields = ['role']

