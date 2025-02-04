from django.urls import path
from recipe import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('chef-special/', views.chef_special, name='chef_special'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    
]
