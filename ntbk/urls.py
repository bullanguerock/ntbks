from django.urls import path
from .views import index, testui

urlpatterns = [
    path('', index),
    path('test', testui),
]