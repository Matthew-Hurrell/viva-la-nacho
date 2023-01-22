from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from django.db.models import Count


# class RecipeList(generic.ListView):
#     model = Recipe
#     queryset = Recipe.objects.filter(status=1).order_by('-created_on')
#     featured_recipe = Recipe.objects.get(featured=True)
#     template_name = 'index.html'
#     paginate_by = 6
#     context_object_name = 'latest_recipe_list'


class RecipeList(generic.ListView):
    model = Recipe
    context_object_name = "data"
    template_name = "index.html"

    def get_queryset(self):
        myset = {
            "latest_recipes": Recipe.objects.filter(status=1).order_by('-created_on'),
            "featured_recipe": Recipe.objects.get(featured=True),
            "most_popular_recipes": Recipe.objects.annotate(like_count=Count('likes')).order_by('-like_count'),
        }
        return myset


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
            },
        )
