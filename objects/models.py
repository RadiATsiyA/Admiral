from django.db import models
from users.models import User
import os


def get_image_path(instance, filename):
    """Функция для распределения изоражений по папкам объектов"""
    return os.path.join('photos', str(instance.object_ad.id), filename)


class ApplicationToView(models.Model):
    TYPE = (
        ('buy', 'Купить'),
        ('sell', 'Продать'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE, default='sale')
    created = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ObjectAd(models.Model):
    """Модель объекта"""
    TYPES = [
        ('flat', 'Квартира'),
        ('house', 'Дом'),
        ('plot', 'Участок'),
        ('office', 'Офис')
    ]
    AD_TYPES = [
        ('rent', 'Аренда'),
        ('sale', 'Продажа')
    ]

    description = models.TextField()
    rooms = models.IntegerField(null=True, blank=True)
    current_floor = models.IntegerField(blank=True, null=True)
    total_floors = models.IntegerField(blank=True, null=True)
    otoplenie = models.CharField(max_length=50, null=True, blank=True)
    remont = models.CharField(max_length=50, null=True, blank=True)
    furniture = models.CharField(max_length=50, null=True, blank=True)
    window_direction = models.CharField(max_length=100, null=True, blank=True)
    area = models.IntegerField()
    type = models.CharField(max_length=15, choices=TYPES, default='flat')
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    year_built = models.IntegerField(default=2010, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    ad_type = models.CharField(max_length=10, choices=AD_TYPES, default='sale')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.address}'


class ObjectFeedback(models.Model):
    """Модель отзывов для объектов"""
    object_ad = models.ForeignKey(ObjectAd, on_delete=models.CASCADE, related_name='feedbacks')
    author = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.author} | {self.object_ad.id}'


class ObjectImage(models.Model):
    """Модель изоражений для объекта"""
    image = models.ImageField(upload_to=get_image_path)
    object_ad = models.ForeignKey(ObjectAd, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.object_ad.id} | {self.image.name}'
    