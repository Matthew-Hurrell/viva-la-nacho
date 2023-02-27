from django.test import TestCase
from .models import Recipe, CATEGORIES, ALLERGIES, DIFFICULTIES, STATUS
from django.contrib.auth.models import User
from django import forms


class RecipeModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            slug='test-recipe',
            author=self.user,
            category=['Food', 'Dinner'],
            featured_image='image.jpg',
            excerpt='Test excerpt',
            prep_time=30,
            cooking_time=60,
            difficulty=1,
            serves=4,
            allergens=['Milk', 'Nuts'],
            ingredients='Test ingredients',
            method='Test method',
            status=1,
            featured=False
        )

    def test_string_of_allergens_method(self):
        """
        Tests that the string_of_allergens method returns a comma separated
        string of allergens.
        """
        allergen_string = self.recipe.string_of_allergens()
        self.assertEqual(allergen_string, 'Milk, Nuts')

    def test_string_of_created_on_method(self):
        """
        Tests that the string_of_created_on method returns a formatted string
        of the created_on date.
        """
        created_on_string = self.recipe.string_of_created_on()
        self.assertEqual(
            created_on_string,
            self.recipe.created_on.strftime("%A %d %B %Y")
        )

    def test_title_max_length(self):
        """
        Tests that the max length of the title field is 200
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_slug_max_length(self):
        """
        Tests that the max length of the slug field is 200
        """
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('slug').max_length
        self.assertEquals(max_length, 200)

    def test_category_choices(self):
        """
        Tests category choices equals categories
        """
        recipe = Recipe.objects.get(id=1)
        choices = recipe._meta.get_field('category').base_field.choices
        self.assertEquals(choices, CATEGORIES)

    def test_allergens_choices(self):
        """
        Tests allergens choices equals allergies
        """
        recipe = Recipe.objects.get(id=1)
        choices = recipe._meta.get_field('allergens').base_field.choices
        self.assertEquals(choices, ALLERGIES)

    def test_difficulty_choices(self):
        """
        Test difficulty choices equals difficulties
        """
        recipe = Recipe.objects.get(id=1)
        choices = recipe._meta.get_field('difficulty').choices
        self.assertEquals(choices, DIFFICULTIES)
