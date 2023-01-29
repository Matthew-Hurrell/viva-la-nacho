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
