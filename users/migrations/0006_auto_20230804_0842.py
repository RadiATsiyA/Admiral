# Generated by Django 3.2.12 on 2023-08-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_agentfeedback_slogan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentfeedback',
            name='slogan',
        ),
        migrations.AddField(
            model_name='agent',
            name='slogan',
            field=models.CharField(default='Нет девиза', max_length=300),
        ),
    ]