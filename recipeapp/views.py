from django.shortcuts import render
from django.views import generic
from .models import Recipe


# class RecipeList(generic.ListView):
#     model = Recipe
#     queryset = Recipe.objects.filter(status=1).order_by('-created_on')
#     featured_recipe = Recipe.objects.get(featured=True)
#     template_name = 'index.html'
#     paginate_by = 6
#     context_object_name = 'latest_recipe_list'


class RecipeList(generic.ListView):
    context_object_name = "data"
    template_name = "index.html"

    def get_queryset(self):
        myset = {
            "latest_recipes": Recipe.objects.filter(status=1).order_by('-created_on'),
            "featured_recipe": Recipe.objects.get(featured=True),
        }
        return myset
