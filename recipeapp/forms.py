from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'category',
            'featured_image',
            'gallery_image_1',
            'gallery_image_2',
            'gallery_image_3',
            'excerpt',
            'prep_time',
            'cooking_time',
            'difficulty',
            'serves',
            'allergens',
            'ingredients',
            'method',
            'status',
        )
