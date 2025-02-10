from django.urls import path, include
from recipe import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('chef-special/', views.chef_special, name='chef_special'),
    path('share/', views.share_recipe, name='share_recipe'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
