from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models
import os


def get_user_image_path(instance, filename):
    """Функция для распределения изоражений по папкам пользователей"""
    return os.path.join('users', str(instance.username), filename)


class User(AbstractUser):
    """Модель начального пользователя
       решил разделить по ролям, что бы не было путаницы
    """
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=get_user_image_path, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_related+",
        related_query_name="%(app_label)s_%(class)ss",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related+",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return f'{self.username}'


class Client(models.Model):
    """Модель клиентов, привязана к пользователям"""
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.user.username}'


class Agent(models.Model):
    """Модель агентов, привязана к пользователям"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    agency_name = models.CharField(max_length=50, null=True, blank=True)
    experience = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f'{self.id} | {self.user.username}'


class AgentFeedback(models.Model):
    """Модель отзывов для Агентов"""
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent_feedbacks')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.author.username} | {self.agent.id}'
