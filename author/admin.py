from django.contrib import admin
from .models import Author
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Author)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
