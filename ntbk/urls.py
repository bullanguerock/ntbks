from django.urls import path
from .views import index, main_view, testfilters, testui, main_view, search_results

urlpatterns = [
    path('', testui),
    path('test', index),
    path('filters', testfilters),
    path('ntbks', main_view),
    path('ntbks/search/', search_results),
]