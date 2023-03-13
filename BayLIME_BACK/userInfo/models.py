from django.db import models
from django.http import JsonResponse

# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birth = models.CharField(max_length=40)






