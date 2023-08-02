from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models
import os


def get_user_image_path(instance, filename):
    """Функция для распределения изоражений по папкам пользователей"""
    return os.path.join('users', str(instance.username), filename)


def get_agent_image_path(instance, filename):
    """Функция для рапределения изображений по папкам агентов"""
    return os.path.join('agents', str(instance.id), filename)


class User(AbstractUser):
    """Модель админа"""
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=get_user_image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'


class Agent(models.Model):
    """Модель агентов, просто хранит информацию об агентах"""
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    agency_name = models.CharField(max_length=50, null=True, blank=True)
    experience = models.FloatField(blank=True, default=0)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to=get_agent_image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.id} | {self.full_name}'


class AgentFeedback(models.Model):
    """Модель отзывов для Агентов"""
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent_feedbacks')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.author.username} | {self.agent.id}'
