# Generated by Django 3.2.12 on 2023-08-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_agent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
