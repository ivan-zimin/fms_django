from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='index'),
    path('visual_control/', visual_control, name='visual_control'),
]

urlpatterns += staticfiles_urlpatterns()