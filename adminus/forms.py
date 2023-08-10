from django.contrib.auth.forms import AuthenticationForm
from users.models import User, Agent, Specialization
from objects.models import ObjectAd, Category, District
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


class ObjectForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control', 'id': 'propertyType'
        })
    )

    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control', 'id': 'district'
        })
    )

    agent = forms.ModelChoiceField(
        required=False,
        queryset=Agent.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control', 'id': 'agent'
        })
    )

    series = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'series'
    }))

    area = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'area'
    }))

    rooms = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'roomCount'
    }))

    current_floor = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'floorCount'
    }))

    total_floors = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'totalfloorCount'
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'company'
    }))

    zastroishik = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'developer'
    }))

    window_direction = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'windowDirection'
    }))

    status = forms.ChoiceField(
        choices=ObjectAd.STATUS,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        })
    )

    images = forms.ImageField(
        required=False,
        label='Добавить фото (до 5 штук):',
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'accept': 'image/*', 'class': 'form-control-file', 'id': 'photos'})
    )

    kitchens_area = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'kitchenArea'
    }))

    otoplenie = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'heating'
    }))

    furniture = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'furniture'
    }))

    balcony = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'balcony'
    }))

    documents = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'legalDocuments'
    }))

    security = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'security'
    }))

    walls_material = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'wallMaterial'
    }))

    ad_type = forms.ChoiceField(
        choices=ObjectAd.AD_TYPES,
        widget=forms.Select(attrs={
            'class': 'form-control', 'id': 'predloj'
        })
    )

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'city'
    }))

    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'id': 'price'
    }))

    class Meta:
        model = ObjectAd
        exclude = ['latitude', 'longitude', 'date_created', ]
















