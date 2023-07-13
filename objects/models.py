from django.db import models
import os


def get_image_path(instance, filename):
    """Функция для распределения изоражений по папкам объектов"""
    return os.path.join('photos', str(instance.object_ad.id), filename)


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

    name = models.CharField(max_length=50)
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


class Feedback(models.Model):
    """Модель отзывов для объектов"""
    object_ad = models.ForeignKey(ObjectAd, on_delete=models.CASCADE, related_name='feedbacks')
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class ObjectImage(models.Model):
    """Модель изоражений для объекта"""
    image = models.ImageField(upload_to=get_image_path)
    object_ad = models.ForeignKey(ObjectAd, related_name='images', on_delete=models.CASCADE)
    