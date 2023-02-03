from . import views
from django.urls import path

# URL Patterns
urlpatterns = [

    # Path for Home
    path('', views.RecipeList.as_view(), name='home'),

    # Path for Liking a Recipe
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),

    # Path for Posting a Recipe
    path('post_recipe/', views.PostRecipe.as_view(), name='post_recipe'),

    # Path for My Recipes 
    path('my_recipes/', views.MyRecipes.as_view(), name='my_recipes'),

    # Path for My Favourites
    path('my_favourites/', views.MyFavourites.as_view(), name='my_favourites'),

    # Path for Unlike Recipe (Remove from My Favourites)
    path('recipe/unlike/<int:pk>', views.UnlikeRecipe.as_view(), name='unlike_recipe'),

    # Path for Edit Recipe 
    path('recipe/edit/<int:pk>/', views.EditRecipe.as_view(), name='edit_recipe'),

    # Path for Delete Recipe
    path('recipe/delete/<int:pk>/', views.DeleteRecipe.as_view(), name='delete_recipe'),

    # Path for Recipe Details
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
]
