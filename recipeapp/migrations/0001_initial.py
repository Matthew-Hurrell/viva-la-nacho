# Generated by Django 3.2.16 on 2023-01-12 21:19

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('gallery_image_1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('gallery_image_2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('gallery_image_3', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('excerpt', models.TextField()),
                ('prep_time', models.PositiveIntegerField()),
                ('cooking_time', models.PositiveIntegerField()),
                ('difficulty', models.CharField(max_length=10)),
                ('serves', models.PositiveIntegerField()),
                ('allergens', models.TextField()),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='recipe_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipeapp.recipe')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
