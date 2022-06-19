# Generated by Django 4.0.5 on 2022-06-19 14:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
