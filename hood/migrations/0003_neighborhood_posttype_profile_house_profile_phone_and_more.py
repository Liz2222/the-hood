# Generated by Django 4.0.5 on 2022-06-18 13:06

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('manager_name', models.CharField(blank=True, max_length=100)),
                ('manager_number', models.CharField(blank=True, max_length=20)),
                ('manager_email', models.EmailField(blank=True, max_length=254)),
                ('hospital_name', models.CharField(blank=True, max_length=100)),
                ('hospital_number', models.CharField(blank=True, max_length=20)),
                ('hospital_email', models.EmailField(blank=True, max_length=254)),
                ('police_name', models.CharField(blank=True, max_length=100)),
                ('police_number', models.CharField(blank=True, max_length=20)),
                ('police_email', models.EmailField(blank=True, max_length=254)),
                ('hood_pic', cloudinary.models.CloudinaryField(default='image/upload/v1627343010/neighborhood1_cj2fyx.jpg', max_length=255, verbose_name='images')),
            ],
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='house',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.neighborhood')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.posttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('start_day', models.CharField(max_length=50)),
                ('end_day', models.CharField(max_length=50)),
                ('open_time', models.CharField(max_length=50)),
                ('close_time', models.CharField(max_length=50)),
                ('bs_image', cloudinary.models.CloudinaryField(default='image/upload/v1627341811/company_default_qb4ili.png', max_length=255, verbose_name='images')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.profile')),
            ],
        ),
    ]
