from django.contrib.sites import requests
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from userInfo import views


router = DefaultRouter()
router.register('user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
