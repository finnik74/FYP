from django.views.decorators.csrf import csrf_exempt
from requests import request
from rest_framework import viewsets
from django.http import HttpResponse
from userInfo.models import Userinfo
from userInfo.serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = Userinfo.objects.all()
    serializer_class = UserSerializer




