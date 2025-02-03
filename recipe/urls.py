from django.urls import path
from recipe import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]
