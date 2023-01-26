from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
