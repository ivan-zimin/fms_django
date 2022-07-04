from django.urls import path
from .views import *

urlpatterns = [
    path('', milling_machine, name='milling_machine'),
]