# Generated by Django 4.0.5 on 2022-06-17 19:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
