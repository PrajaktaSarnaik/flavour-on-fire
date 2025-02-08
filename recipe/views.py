from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm
from .forms import RecipeForm

@login_required
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
    and displays them in a page of six recipes.
    **Context**

    ``queryset``
        All published instances of :model:`recipe.Recipe`
    ``paginate_by``
        Number of recipes per page.

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

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_detail.html`
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "recipe/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        print("Comment:", comment)  # Debug print
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))



@login_required
def share_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.status = 0  # Set status to 'Draft' for admin approval
            recipe.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing your recipe! It's on its way for approval and will be live in the Recipe section once it's approved. Stay tuned!")
            form = RecipeForm()
            # return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Error submitting recipe!')
    else:
        form = RecipeForm()
    return render(request, 'recipe/share_recipe.html', {'form': form})