from django.urls import path
from .views import index, testui

urlpatterns = [
    path('', testui),
    path('test', index),
]