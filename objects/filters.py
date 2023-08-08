import django_filters
from django import forms
from .models import ObjectAd, District, Category


class ObjectAdFilter(django_filters.FilterSet):
    series = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'filter-input'}),
        label='Серия',
    )

    district = django_filters.ModelChoiceFilter(
        empty_label='Все',
        queryset=District.objects.all(),  # Use queryset from the database
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


class MapObjectFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'form-select mb-3 w-50'}),
        label='Тип недвижимости'
    )

    district = django_filters.ModelChoiceFilter(
        empty_label='Все',
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select mb-3 w-50'}),
        label='Район',
    )

    ROOM_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4+'),
    ]

    rooms = django_filters.ChoiceFilter(
        empty_label="Все",
        choices=ROOM_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select mb-3 w-50'}),
        label='Количество комнат'
    )

    series = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-select mb-3 w-50', 'placeholder': '105'}),
        label='Серия',
    )

    priceFrom = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена от'}),
        label='Цена от',
    )

    priceTo = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена до'}),
        label='Цена до',
    )

    class Meta:
        model = ObjectAd
        fields = ['category', 'district', 'rooms', 'series', 'price']
