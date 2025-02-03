from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('recipe_title', 'slug', 'status')
    search_fields = ['recipe_title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('recipe_title',)}
    summernote_fields = ('ingredients', 'instructions')


# Register your models here.

admin.site.register(Comment)

