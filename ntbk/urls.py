from django.urls import path
from .views import index, main_view, testfilters, testui, main_view, search_results

urlpatterns = [
    path('', testui),
    path('test', index),
    path('filters', testfilters),
    path('ajax', main_view),
    path('ajax/search/', search_results),
]