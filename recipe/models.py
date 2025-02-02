from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS_CHOICES = (
    ('0', 'Draft'),
    ('1', 'Published'),
    )
DIET_CHOICES = (
    ('0', 'Vegetarian'),
    ('1', 'Non-Vegetarian'),
    ('2', 'Vegan'),
    )


# Create your models here.
# class Recipe(models.Model):
#     recipe_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe_title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     author = models.ForeignKey(User, related_name='recipe_author', on_delete=models.CASCADE)
#     featured_image = CloudinaryField('image', default='placeholder')
#     diet = models.CharField(max_length=10, choices=DIET_CHOICES)
#     introduction = models.TextField()
#     instructions = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#     excerpt = models.TextField(max_length=500, blank=True)

#     def __str__(self):
#         return self.recipe_title