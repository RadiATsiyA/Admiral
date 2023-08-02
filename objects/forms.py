import django_filters
from django import forms
from .models import ApplicationToView


class ApplicationToViewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'animate-slide-up-fade-in form-control border-0 rounded-pill w-50',
        'placeholder': 'Имя',
        'id': 'inputName',
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'animate-slide-up-fade-in form-control border-0 rounded-pill w-50',
        'placeholder': 'Номер телефона',
        'id': 'inputPhoneNumber',
    }))

    TYPE_CHOICES = (
        ('buy', 'Купить'),
        ('sell', 'Продать'),
    )

    type = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class': 'animate-slide-up-fade-in form-check-inline',
    }), choices=TYPE_CHOICES)

    class Meta:
        model = ApplicationToView
        fields = ['name', 'phone', 'type']
