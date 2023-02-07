from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField


class ModifiedArrayField(ArrayField):
    """
    Modified Array Field.
    Allows for checkbox multiple select fields to create an array.
    """

    def formfield(self, **kwargs):

        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple,
            **kwargs
        }
        return super(ArrayField, self).formfield(**defaults)


# Status Choices
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

# Categories Choices
CATEGORIES = (
    ('Food', 'Food'),
    ('Drink', 'Drink'),
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Desert', 'Desert'),
    ('Tacos', 'Tacos'),
    ('Enchiladas', 'Enchiladas'),
    ('Tostadas', 'Tostadas'),
    ('Chilaquiles', 'Chilaquiles'),
    ('Huevos Rancheros', 'Huevos Rancheros'),
    ('Machaca', 'Machaca'),
    ('Discada', 'Discada'),
    ('Burritos', 'Burritos'),
    ('Menudo', 'Menudo'),
    ('Tamales', 'Tamales'),
    ('Quesadilla', 'Quesadilla'),
    ('Esquites', 'Esquites'),
    ('Fajitas', 'Fajitas'),
    ('Carnitas', 'Carnitas'),
    ('Chilli Con Carne', 'Chilli Con Carne'),
    ('Vegetarian', 'Vegetarian'),
    ('Vegan', 'Vegan'),
    ('Gluten Free', 'Gluten Free')
)

# Allergies Choices
ALLERGIES = (
    ('Celery', 'Celery'),
    ('Crustaceans', 'Crustaceans'),
    ('Fish', 'Fish'),
    ('Milk', 'Milk'),
    ('Mustard', 'Mustard'),
    ('Peanuts', 'Peanuts'),
    ('Soya', 'Soya'),
    ('Gluten', 'Gluten'),
    ('Eggs', 'Eggs'),
    ('Lupin', 'Lupin'),
    ('Molluscs', 'Molluscs'),
    ('Nuts', 'Nuts'),
    ('Sesame Seeds', 'Sesame Seeds'),
    ('Sulphur Dioxide', 'Sulphur Dioxide'),
    ('None', 'None')
)

# Difficulties Choices
DIFFICULTIES = (
    (0, 'Beginner'),
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
    (4, 'Pro')
)


class Recipe(models.Model):
    """
    Recipe model class.
    Assigns fields and methods for the recipe model.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    category = ModifiedArrayField(
        models.CharField(
            choices=CATEGORIES,
            max_length=100
        )
    )
    featured_image = CloudinaryField('image', default='placeholder')
    gallery_image_1 = CloudinaryField('image', blank=True, null=True)
    gallery_image_2 = CloudinaryField('image', blank=True, null=True)
    gallery_image_3 = CloudinaryField('image', blank=True, null=True)
    excerpt = models.TextField()
    prep_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    difficulty = models.IntegerField(choices=DIFFICULTIES)
    serves = models.PositiveIntegerField()
    allergens = ModifiedArrayField(
        models.CharField(
            choices=ALLERGIES,
            max_length=100
        )
    )
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name="recipe_likes",
        blank=True
    )
    featured = models.BooleanField(default=False)

    class Meta:

        ordering = ['-created_on']

    # Title String Function
    def __str__(self):
        return self.title

    # Count Number of Likes Function
    def number_of_likes(self):
        return self.likes.count()

    # Combine Allergens Array Into String Function
    def string_of_allergens(self):
        return ', '.join(self.allergens)

    # Format Date of Created On Function
    def string_of_created_on(self):
        return self.created_on.strftime("%A %d %B %Y")


class Comment(models.Model):
    """
    Comment model.
    Assigns fields and methods for the comment model.
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:

        ordering = ['created_on']

    # Title String Function
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    # Format Date of Created On Function
    def string_of_created_on(self):
        return self.created_on.strftime("%A %d %B %Y")
