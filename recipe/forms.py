from .models import Comment, RATING_STARS
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=RATING_STARS),
        }