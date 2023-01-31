from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('post_recipe/', views.PostRecipe.as_view(), name='post_recipe'),
    path('my_recipes/', views.MyRecipes.as_view(), name='my_recipes'),
    path('recipe/edit/<int:pk>/', views.EditRecipe.as_view(), name='edit_recipe'),
    path('recipe/delete/<int:pk>/', views.DeleteRecipe, name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
]
