# Generated by Django 3.2.12 on 2023-08-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='Category'),
        ),
    ]
