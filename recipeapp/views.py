from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from django.db.models import Count
from .forms import CommentForm, RecipeForm
from django.template.defaultfilters import slugify


class RecipeList(generic.ListView):
    model = Recipe
    context_object_name = "data"
    template_name = "index.html"

    def get_queryset(self):
        myset = {
            "latest_recipes": Recipe.objects.filter(status=1).order_by('-created_on'),
            "featured_recipe": Recipe.objects.get(featured=True),
            "most_popular_recipes": Recipe.objects.filter(status=1).annotate(like_count=Count('likes')).order_by('-like_count'),
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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class PostRecipe(View):

    form_class = RecipeForm
    initial = {'key': 'value'}
    template_name = 'post_recipe.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False,
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            recipe = form.save(commit=False)
            recipe.save()
            print('successful')
            return render(
                request,
                'post_recipe.html',
                {
                    'posted': True,
                }
            )
        else:
            print('unsuccessful')
            return render(
                request,
                'post_recipe.html',
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


class MyRecipes(generic.ListView):
    model = Recipe
    template_name = 'my_recipes.html'

    def get(self, request):
        queryset = Recipe.objects.filter(author=request.user.id).order_by('-created_on')
        queryset_dict = {
            'my_recipes': queryset
        }
        return render(
            request,
            self.template_name,
            queryset_dict
         )
