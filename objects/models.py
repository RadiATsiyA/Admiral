from django.db import models
from users.models import User, Agent
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


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class District(models.Model):
    district_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_name


class ObjectAd(models.Model):
    """Модель объекта"""
    AD_TYPES = [
        ('Аренда', 'Аренда'),
        ('Продажа', 'Продажа')
    ]

    STATUS = [
        ('completed', 'Завершен'),
        ('incomplete', 'Не завершен')
    ]

    rooms = models.IntegerField(null=True, blank=True)
    current_floor = models.IntegerField(blank=True, null=True)
    total_floors = models.IntegerField(blank=True, null=True)
    otoplenie = models.CharField(max_length=50, null=True, blank=True)
    # remont = models.CharField(max_length=50, null=True, blank=True)
    furniture = models.CharField(max_length=50, null=True, blank=True)
    balcony = models.CharField(max_length=50, null=True, blank=True)
    series = models.IntegerField(null=True, blank=True)
    window_direction = models.CharField(max_length=100, null=True, blank=True)
    security = models.CharField(max_length=50, null=True, blank=True)
    area = models.IntegerField()
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=30, null=True, blank=True)  # Широта
    longitude = models.CharField(max_length=30, null=True, blank=True)  # Долгота
    # year_built = models.IntegerField(default=2010, null=True, blank=True)
    zastroishik = models.CharField(max_length=50, null=True, blank=True)
    ad_type = models.CharField(max_length=10, choices=AD_TYPES, default='Продажа')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    kitchens_area = models.IntegerField()
    documents = models.CharField(max_length=50, null=True, blank=True)
    walls_material = models.CharField(max_length=50, null=True, blank=True)
    # is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS, blank=True, null=True, default='completed')
    category = models.ForeignKey(to=Category, related_name='category', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(to=District, related_name='district', on_delete=models.SET_NULL, null=True, blank=True)
    agent = models.ForeignKey(to=Agent, related_name='agent_object', on_delete=models.SET_NULL, null=True, blank=True)

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
    