# Generated by Django 4.0.5 on 2022-06-19 09:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_alter_business_bs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='images'),
        ),
    ]
