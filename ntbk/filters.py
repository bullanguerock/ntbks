import django_filters
from django_filters.filters import CharFilter

from .models import Note

class NtbkFilter(django_filters.FilterSet):

    nombre = CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = Note
        fields = ['ramint', 'precio']