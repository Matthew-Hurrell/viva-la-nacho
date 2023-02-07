from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Comment Form Class.
    Sets the model and fields for the comment form.
    """

    class Meta:

        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Recipe Form Class.
    Sets the model and fields for the recipe form.
    Also assigns summernote widget to certain form fields.
    """

    class Meta:

        model = Recipe

        # Summernote Widgets
        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget()
        }

        fields = (
            'title',
            'category',
            'prep_time',
            'cooking_time',
            'serves',
            'difficulty',
            'excerpt',
            'allergens',
            'ingredients',
            'method',
            'featured_image',
            'gallery_image_1',
            'gallery_image_2',
            'gallery_image_3',
            'status',
        )
