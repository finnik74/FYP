"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from demoproject import view

from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',view.auth),
    path('api/', include('userInfo.urls')),
    path('register/',view.user_register),
    path('bay/',view.bay),
    path('lime_demo/',view.limeDemo),
    path('upload/',view.upload),
    path('baylime_load/',view.load_sp),
    path('verify/',view.verify_sp),
    path('baylime_predict/',view.baylime_predict),
    path('download_csv/', view.download_csv, name='download_csv'),
    path('delete-folder/', view.delete_folder),

]

