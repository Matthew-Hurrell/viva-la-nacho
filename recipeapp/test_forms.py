from django.test import TestCase
from .forms import RecipeForm, CommentForm


# class TestRecipeForm(TestCase):

#     def test_recipe_title_is_required(self):
#         form = RecipeForm({'title': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('title', form.errors.keys())
#         self.assertEqual(form.errors['title'][0], 'This field is required.')
