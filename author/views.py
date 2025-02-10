from django.shortcuts import render
from .models import Author


def about_me(request):
    """
    Renders the Author page
    """
    authors = Author.objects.all().order_by('-updated_on')

    return render(
        request,
        "author/author.html",
        {"authors": authors},
    )
