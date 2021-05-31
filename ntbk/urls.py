from django.urls import path
from .views import index, main_view, testfilters, testui, main_view, search_results

urlpatterns = [
    path('', testfilters),
    path('old', index),
    path('mixitup', testui),
    path('ntbks', main_view),
    path('ntbks/search/', search_results),
]