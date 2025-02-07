from django.shortcuts import render
from .models import Author


def about_me(request):
    """
    Renders the Author page
    """
    author = Author.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "author/author.html",
        {"author": author},
    )