# Generated by Django 3.2.16 on 2023-01-13 20:55

import cloudinary.models
from django.db import migrations, models
import recipeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergens',
            field=recipeapp.models.ModifiedArrayField(base_field=models.CharField(choices=[('Celery', 'Celery'), ('Crustaceans', 'Crustaceans'), ('Fish', 'Fish'), ('Milk', 'Milk'), ('Mustard', 'Mustard'), ('Peanuts', 'Peanuts'), ('Soya', 'Soya'), ('Gluten', 'Gluten'), ('Eggs', 'Eggs'), ('Lupin', 'Lupin'), ('Molluscs', 'Molluscs'), ('Nuts', 'Nuts'), ('Sesame Seeds', 'Sesame Seeds'), ('Sulphur Dioxide', 'Sulphur Dioxide')], max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=recipeapp.models.ModifiedArrayField(base_field=models.CharField(choices=[('Food', 'Food'), ('Drink', 'Drink'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Desert', 'Desert'), ('Tacos', 'Tacos'), ('Enchiladas', 'Enchiladas'), ('Tostadas', 'Tostadas'), ('Chilaquiles', 'Chilaquiles'), ('Huevos Rancheros', 'Huevos Rancheros'), ('Machaca', 'Machaca'), ('Discada', 'Discada'), ('Burritos', 'Burritos'), ('Menudo', 'Menudo'), ('Tamales', 'Tamales'), ('Quesadilla', 'Quesadilla'), ('Esquites', 'Esquites'), ('Fajitas', 'Fajitas'), ('Carnitas', 'Carnitas'), ('Chilli Con Carne', 'Chilli Con Carne'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Gluten Free', 'Gluten Free')], max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='gallery_image_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='gallery_image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='gallery_image_3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]