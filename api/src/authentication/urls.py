from django.urls import path
from django.urls.conf import include, include
from rest_framework import routers
from .views import RegisterApiView, LoginApiView

router = routers.DefaultRouter()
#router.register('role',CustonRoleViewset)


urlpatterns = [
    path('register/',RegisterApiView.as_view(), name = 'registration'),
    path('login/',LoginApiView.as_view(), name = 'registration'),
   # path('', include(router.urls)),
]
