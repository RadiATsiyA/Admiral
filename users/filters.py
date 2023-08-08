import django_filters
from django import forms
from .models import Agent, Specialization
from objects.models import District


class AgentFilter(django_filters.FilterSet):
    district = django_filters.ModelChoiceFilter(
        queryset=District.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'filter-select', 'id': 'district'}),
        label='Район',
    )

    specialization = django_filters.ModelChoiceFilter(
        queryset=Specialization.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'filter-select', 'id': 'district'}),
        label='Специализация',
    )

    class Meta:
        model = Agent
        fields = ['district', 'specialization']
