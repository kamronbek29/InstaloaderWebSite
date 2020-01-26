from django.urls import path

from .views import *

urlpatterns = [
    path('', instaloader, name='instaloader'),
]
