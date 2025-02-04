from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Recipe


def chef_special(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Display recipes only by 'Admin'
        recipes = Recipe.objects.filter(author__username='Admin', status=1)
        return render(request, 'recipe/chef_special.html', {'recipe_list': recipes})
    else:
        # Redirect to the login page with a 'next' parameter
        return redirect('account_login')  


class RecipeList(generic.ListView):
    """
    Returns all published recipes in :model:`recipe.Recipe`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`recipe.Recipe`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`recipe/index.html`
    """

    queryset = Recipe.objects.all().filter(status=1)
    template_name = "recipe/index.html"
    paginate_by = 6

    def get_queryset(self):
        recipes = Recipe.objects.filter(status=1)
        print("All Recipes:", recipes)  # Debug print

        filtered_recipes = recipes.exclude(author__username='Admin')
        print("Filtered Recipes (excluding admin):", filtered_recipes)  # Debug print

        return filtered_recipes
    

def recipe_detail(request, slug):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``post``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipe/recipe_detail.html",
        {"recipe": recipe},
    )

