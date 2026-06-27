import django_filters
from .models import CashFlow

class CashFlowFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte', label='Дата с')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte', label='Дата по')

    class Meta:
        model = CashFlow
        fields = ['status', 'cash_type', 'category', 'subcategory', 'date_from', 'date_to']