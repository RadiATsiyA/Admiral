import django_filters
from django import forms
from .models import ObjectAd


class ObjectAdFilter(django_filters.FilterSet):
    series = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'filter-input'}),
        label='Серия',
    )

    district = django_filters.ChoiceFilter(
        choices=[
            ('', 'Выберите Район'),
            ('Ленинский', 'Ленинский'),
            ('Свердловский', 'Свердловский'),
            ('Октябрьский', 'Октябрьский')
        ],
        widget=forms.Select(attrs={'class': 'filter-select'}),
        label='Район',
    )

    area = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'filter-input'}),
        label='Площадь',
    )

    priceFrom = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class': 'filter-input'}),
        label='Цена от',
    )

    priceTo = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class': 'filter-input'}),
        label='Цена до',
    )

    class Meta:
        model = ObjectAd
        fields = ['price', 'district', 'area', 'series']
