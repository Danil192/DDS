import django_filters
from django import forms
from .models import CashFlow

class CashFlowFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='gte', 
        label='Дата с',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    date_to = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='lte', 
        label='Дата по',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = CashFlow
        fields = ['status', 'cash_type', 'category', 'subcategory', 'date_from', 'date_to']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'cash_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
        }