from .models import Recipe, Comment, RATING_STARS
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=RATING_STARS),
        }

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_title', 'featured_image', 'diet', 'introduction', 'ingredients', 'instructions']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4}),
            'instructions': forms.Textarea(attrs={'rows': 4}),
        }