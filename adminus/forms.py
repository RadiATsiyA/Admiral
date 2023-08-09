from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User, Agent, Specialization
from objects.models import ObjectAd
from django import forms


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'username', 'name': 'username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'password', 'name': 'password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class AgentForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'fullName', 'required': True
    }))

    agency_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'company'
    }))

    experience = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'experience'
    }))

    specialization = forms.ModelMultipleChoiceField(
        queryset=Specialization.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        })
    )

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'phone'
    }))

    slogan = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'slogan'
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'custom-file-input', 'id': 'photo', 'accept': 'image/*', 'onchange': 'previewImage(this);'
    }))

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial_specializations = instance.specialization.all()
            kwargs['initial'] = {'specialization': initial_specializations}
        super().__init__(*args, **kwargs)

    class Meta:
        model = Agent
        fields = ['full_name', 'experience', 'specialization', 'phone', 'agency_name', 'slogan', 'image']
