from django.contrib import admin
from django.urls import path
from ipgetter.views import get_ip

urlpatterns = [
    path('get/', get_ip, name='ipgetter'),
]
