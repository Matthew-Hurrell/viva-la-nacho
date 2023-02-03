from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from django.db.models import Count
from .forms import CommentForm, RecipeForm
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView


class RecipeList(generic.ListView):
    """
    RecipeList (Homepage) class view.
    Defines model and template name as well as context object name.
    Defines method which returns two lists of objects and one single object.
    """

    # Model
    model = Recipe

    # Context Object Name
    context_object_name = "recipes"

    # Template Name
    template_name = "index.html"

    # Get Method
    def get_context_data(self, **kwargs):
        """
        Get method returning most popular recipes list, latest recipes list and featured recipe.
        """

        context = super().get_context_data(**kwargs)

        # Latest Recipes List
        context['latest_recipes'] = Recipe.objects.filter(status=1).order_by('-created_on')[:9]

        # Most Popular Recipes List
        context['most_popular_recipes'] = Recipe.objects.filter(status=1).annotate(like_count=Count('likes')).order_by('-like_count')[:9]

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

        # Queryset Filtering Out Draft Recipes
        queryset = Recipe.objects.filter(status=1)

        # Assigning Recipe Instance to recipe Variable
        recipe = get_object_or_404(queryset, slug=slug)

        # Assigning Approved Recipe Comments to comments Variable
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        # Set liked to False
        liked = False

        # Set liked to True if User has Liked Recipe
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Return Render Request with Template Name and Variables
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
        Post method for comment form setting recipe object and returning variables.
        """

        # Queryset Filtering Out Draft Recipes
        queryset = Recipe.objects.filter(status=1)

        # Assigning Recipe Instance to recipe Variable
        recipe = get_object_or_404(queryset, slug=slug)

        # Assigning Recipe Comments to comments Variable
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        # Set liked to False
        liked = False

        # If User has Liked Recipe, Set liked to True
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Assign Comment Form to comment_form Variable
        comment_form = CommentForm(data=request.POST)

        # If comment_form is Valid
        if comment_form.is_valid():

            # Assign User Email to Comment Form Email Field
            comment_form.instance.email = request.user.email

            # Assign User Username to Comment Form Name
            comment_form.instance.name = request.user.username

            # Assign Comment Form to comment Variable With Commit Set to False
            comment = comment_form.save(commit=False)

            # Match Comment to Recipe 
            comment.recipe = recipe

            # Save Comment
            comment.save()

        # If comment_form Isn't Valid
        else:
            comment_form = CommentForm()

        # Return Render Request with Template Name and Variables
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

        # Assign Recipe Object to recipe Variable 
        recipe = get_object_or_404(Recipe, slug=slug)

        # If User has Already Liked Recipe
        if recipe.likes.filter(id=request.user.id).exists():

            # Remove User From Recipe Likes
            recipe.likes.remove(request.user)

        # Otherwise if User Hasn't Liked Recipe
        else:

            # Add User to Recipe Likes
            recipe.likes.add(request.user)

        # Return Redirect Reverse to recipe_details Template
        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class PostRecipe(View):
    """
    PostRecipe class view.
    Uses with the RecipeForm on the post_recipe template to allow users to post a recipe.
    Class features a get and a post method to render the template and post the form.
    """

    # Assign RecipeForm to form_class Variable
    form_class = RecipeForm

    # Set Key and Value Object to initial Variable
    initial = {'key': 'value'}

    # Assign post_recipe Template to template_name Variable
    template_name = 'post_recipe.html'

    def get(self, request, *args, **kwargs):
        """
        Get method to render template and return variables.
        """

        # Set form Variable to form_class with initial variable Passed as Argument
        form = self.form_class(initial=self.initial)

        # Return Render Request with Template Name and Variables
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

        # Assign form_class with Post and Files Arguments to form Variable
        form = self.form_class(request.POST, request.FILES)

        # If Form is Valid
        if form.is_valid():

            # Assign User to Recipe Form Instance Field
            form.instance.author = request.user

            # Assign Slugified Form Instance Title to Form Instance Slug
            form.instance.slug = slugify(form.instance.title)

            # Assign Uncommitted form to recipe Variable
            recipe = form.save(commit=False)

            # Save Recipe
            recipe.save()

            # Return Render Request with post_recipe template and posted Variable Set to True
            return render(
                request,
                'post_recipe.html',
                {
                    'posted': True,
                }
            )

        # If Form Isn't Valid
        else:
            
            # Return Render Request with post_recipe Template with Failed Variable Set to True
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
    Pulls in data from a specific recipe object and fills it into form fields for editing.
    edit_recipe template is used to render the form.
    """

    # Sets Recipe as Model
    model = Recipe

    # Sets the edit_recipe Template as the Template Name
    template_name = 'edit_recipe.html'

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to render template and form.
        """

        # Assigns Specific Recipe Object Using Primary Key Field to recipe Variable 
        recipe = Recipe.objects.get(pk=pk)

        # Creates An Instance of the RecipeForm with the recipe object
        form = RecipeForm(instance=recipe)

        # Render Request with Template Name and Variables
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

        # Assigns Specific Recipe Object Using Primary Key Field to recipe Variable 
        recipe = Recipe.objects.get(pk=pk)

        # Passes Recipe Instance, Post Request and Files Request to RecipeForm and Assigns form to form Variable
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        # If Form Is Valid
        if form.is_valid():

            # Save Form
            form.save()

            # Assign Slugify Form Instance Title to Form Instance Slug
            form.instance.slug = slugify(form.instance.title)

            # Assign Uncommited Form to recipe Variable
            recipe = form.save(commit=False)

            # Save Recipe
            recipe.save()

            # Return Render Request with Template Name and Variables
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'posted': True
                }
            )

        # If Form Isn't Valid
        else:

            # Return Render Request with Template Name and Variables Including Failed True
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

    # Sets Recipe as Model
    model = Recipe

    # Assigns my_recipes Template to template_name Variable
    template_name = 'my_recipes.html'

    def get(self, request):
        """
        Get method to render template and return queryset objects.
        """

        # Set queryset to Recipe Objects Which Have Been Created By The User
        queryset = Recipe.objects.filter(author=request.user.id).order_by('-created_on')

        # Queryset Dictionary
        queryset_dict = {
            'my_recipes': queryset
        }

        # Return Render Request with my_recipes Template and queryset
        return render(
            request,
            self.template_name,
            queryset_dict
        )


class MyFavourites(generic.ListView):
    """
    MyFavourites class view.
    Returns a list of recipe objects that a user has liked to the my_favourites template.
    """

    def get(self, request, *args, **kwargs):
        """
        Get method to render template and return queryset objects.
        """

        # Assign User Request to user Variable
        user = request.user

        # Filter Recipe Objects to Display Published Recipes That The User Has Liked
        favourite_recipes = Recipe.objects.filter(likes=user).filter(status=1)

        # Assign favourite_recipes Variable to context Object
        context = {'recipes': favourite_recipes}

        # Return Render Request with my_favourites Template and Context Object
        return render(request, 'my_favourites.html', context)


class DeleteRecipe(View):
    """
    DeleteRecipe class view.
    Deletes specific recipe object using the primary key. 
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to delete recipe object.
        """

        # Assign Recipe Object Using Primary Key to recipe Variable
        recipe = get_object_or_404(Recipe, pk=pk)

        # Delete recipe
        recipe.delete()

        # Return Redirect to Template my_recipes
        return redirect('my_recipes')


class UnlikeRecipe(View):
    """
    UnlikeRecipe class view.
    Used to remove recipe from my_favourites template user list.
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to remove recipe from user my_favourites list by unliking recipe.
        """

        # Assign Recipe Object Using Primary Key to recipe Variable
        recipe = get_object_or_404(Recipe, pk=pk)

        # Remove User Like from Recipe
        recipe.likes.remove(request.user)

        # Return Redirect to Template my_favourites
        return redirect('my_favourites')
