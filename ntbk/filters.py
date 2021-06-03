from django.db.models.fields import BooleanField
from django.forms.widgets import Input, Select
import django_filters
from django_filters import widgets
from django_filters.filters import BooleanFilter, CharFilter , AllValuesFilter, NumberFilter , RangeFilter, ChoiceFilter

from .models import Note

from django.db.models import Q


FILTER_CHOICES = (
    ('', 'Todos'),
    ('GB', 'Gamer'),
    ('No tar', 'Oficina')
)

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

    q = CharFilter(method=multiple_search, widget=Input(attrs={ 'type' : 'search',
                                                                'placeholder' : '...',
                                                                'autocomplete' : 'off',
                                                               }))
    g = CharFilter(field_name='gpuDedi', lookup_expr='icontains')
    ramint = AllValuesFilter(field_name='ramint', widget=Select(attrs={ 'class' : 'filter'}))
    p = RangeFilter(field_name='precioint')
    tipo = ChoiceFilter(field_name='gpuDedi', choices=FILTER_CHOICES, lookup_expr='icontains')

    class Meta:
        model = Note
        fields = ['precioint']
        