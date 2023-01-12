from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    category = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    gallery_image_1 = CloudinaryField('image')
    gallery_image_2 = CloudinaryField('image')
    gallery_image_3 = CloudinaryField('image')
    excerpt = models.TextField()
    prep_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=10)
    serves = models.PositiveIntegerField()
    allergens = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="recipe_likes")
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
