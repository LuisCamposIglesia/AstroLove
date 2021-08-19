import django_filters
from .models import *
from django.forms.widgets import TextInput
class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label="Título")
    date = django_filters.DateFilter(field_name="date", label="Fecha",
                                      widget=TextInput(attrs={'placeholder': 'dd/mm/yyyy'}))
    class Meta:
        model = Evento
        fields = ["id"]
        exclude = ["id"]

class ChatFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains', label="Nombre")
    class Meta:
        model = Usuario
        fields = ["id"]
        exclude = ["id"] 