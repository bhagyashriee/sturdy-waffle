from django.urls import path
from . import views

urlpatterns = [
    # path('search-food/', views.search_food, name='search_food'),
    path('get-nutrition/', views.get_nutrition, name='get_nutrition'),
    path('recipe/', views.recipe_view, name='recipe'),
]
