from django.urls import path
from rest_framework import routers
from .views import RegisterApiView, LoginApiView, UserApiView

router = routers.DefaultRouter()


urlpatterns = [
    path('register/',RegisterApiView.as_view(), name = 'registration'),
    path('login/',LoginApiView.as_view(), name = 'registration'),
    path('users/',UserApiView.as_view(), name = 'users'),
]
