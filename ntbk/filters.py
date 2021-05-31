from django.db.models.fields import BooleanField
import django_filters
from django_filters.filters import BooleanFilter, CharFilter

from .models import Note

from django.db.models import Q

def multiple_search(queryset, name, value):
    queryset = queryset.filter(
                                Q(nombre__icontains=value) | 
                                Q(proce__icontains=value) |
                                Q(gpu__icontains=value) |
                                Q(gpuDedi__icontains=value) |
                                Q(ram__icontains=value)
                              )
    return queryset

class NtbkFilter(django_filters.FilterSet):

    q = CharFilter(method=multiple_search)
    g = CharFilter(field_name='gpuDedi', lookup_expr='icontains')

    class Meta:
        model = Note
        fields = ['ramint', 'precio']