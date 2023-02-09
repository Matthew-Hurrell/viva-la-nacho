from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Recipe, Comment
from django.db.models import Count
from .forms import CommentForm, RecipeForm
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from django.contrib import messages


class RecipeList(generic.ListView):
    """
    RecipeList (Homepage) class view.
    Defines model and template name as well as context object name.
    Defines method which returns two lists of objects and one single object.
    """

    model = Recipe
    context_object_name = "recipes"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        Get method returning most popular recipes list, latest recipes list
        and featured recipe.
        """

        context = super().get_context_data(**kwargs)

        # Latest Recipes List
        context['latest_recipes'] = Recipe.objects.filter(
            status=1).order_by('-created_on')[:9]

        # Most Popular Recipes List
        context['most_popular_recipes'] = Recipe.objects.filter(
            status=1).annotate(like_count=Count('likes')).order_by(
                '-like_count')[:9]

        # Featured Recipe
        context['featured_recipe'] = Recipe.objects.get(featured=True)

        return context


class RecipeDetails(View):
    """
    RecipeDetails class view.
    Returns full details of a specific recipe to the recipe_details template.
    Features get and post methods.
    Post method for posting a comment.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get method setting recipe object and returning variables.
        """

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
        """
        Post method for comment form setting recipe object and returning
        variables.
        """

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
    """
    RecipeLike class view.
    Contains post method for liking and unliking a recipe.
    """

    def post(self, request, slug):
        """
        Post method for liking and unliking a recipe.
        """

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class PostRecipe(View):
    """
    PostRecipe class view.
    Uses with the RecipeForm on the post_recipe template to allow users
    to post a recipe.
    Class features a get and a post method to render the template and
    post the form.
    """

    form_class = RecipeForm
    initial = {'key': 'value'}
    template_name = 'post_recipe.html'

    def get(self, request, *args, **kwargs):
        """
        Get method to render template and return variables.
        """

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
        """
        Post method to submit and save form to new recipe instance.
        """
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            recipe = form.save(commit=False)
            recipe.save()
            return render(
                request,
                'post_recipe.html',
                {
                    'posted': True,
                }
            )
        else:
            return render(
                request,
                'post_recipe.html',
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


class EditRecipe(TemplateView):
    """
    EditRecipe class view.
    Features a get and a post method.
    Pulls in data from a specific recipe object and fills it into form fields
    for editing. edit_recipe template is used to render the form.
    """

    model = Recipe
    template_name = 'edit_recipe.html'

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to render template and form.
        """

        recipe = Recipe.objects.get(pk=pk)
        form = RecipeForm(instance=recipe)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False
            }
        )

    def post(self, request, pk, *args, **kwargs):
        """
        Post method to submit recipe form and return template with variables.
        """

        recipe = Recipe.objects.get(pk=pk)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            form.instance.slug = slugify(form.instance.title)
            recipe = form.save(commit=False)
            recipe.save()

            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'posted': True
                }
            )
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


class MyRecipes(generic.ListView):
    """
    MyRecipes class view.
    Returns list of recipe objects created by user to the my_recipes template.
    """

    model = Recipe
    template_name = 'my_recipes.html'

    def get(self, request):
        """
        Get method to render template and return queryset objects.
        """

        queryset = Recipe.objects.filter(
            author=request.user.id).order_by('-created_on')
        queryset_dict = {
            'my_recipes': queryset
        }

        return render(
            request,
            self.template_name,
            queryset_dict
        )


class MyFavourites(generic.ListView):
    """
    MyFavourites class view.
    Returns a list of recipe objects that a user has liked to
    the my_favourites template.
    """

    def get(self, request, *args, **kwargs):
        """
        Get method to render template and return queryset objects.
        """

        user = request.user
        favourite_recipes = Recipe.objects.filter(likes=user).filter(status=1)
        context = {'recipes': favourite_recipes}

        return render(request, 'my_favourites.html', context)


class DeleteRecipe(View):
    """
    DeleteRecipe class view.
    Deletes specific recipe object using the primary key and returns
    recipe_deleted template.
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to delete recipe object.
        """
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        messages.success(request, 'Recipe deleted')

        return redirect(reverse('my_recipes'))


class UnlikeRecipe(View):
    """
    UnlikeRecipe class view.
    Used to remove recipe from my_favourites template user list.
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to remove recipe from user my_favourites list by
        unliking recipe.
        """

        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.likes.remove(request.user)
        messages.success(request, 'Recipe unliked')

        return redirect(reverse('my_favourites'))


class AllRecipes(generic.ListView):
    """
    AllRecipes class view.
    Returns list of all published recipes to the all_recipes template.
    """

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'all_recipes.html'
    paginate_by = 9


# 404 View
def custom_404(request, exception):
    return render(request, "404.html")
