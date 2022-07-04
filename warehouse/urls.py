from django.urls import path
from .views import *

urlpatterns = [
    path('', warehouse_page, name='warehouse_page'),
]