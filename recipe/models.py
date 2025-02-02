from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
    )
DIET = (
    (0, 'Vegetarian'),
    (1, 'Non-Vegetarian'),
    (2, 'Vegan'),
    (3, 'Other'),
    )


# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, related_name='recipe_author', on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    diet = models.IntegerField(choices=DIET, default=3)
    introduction = models.TextField()
    
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.recipe_title} | written by {self.author}"