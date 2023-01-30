from django.contrib import admin
from .models import Post, Comment
from djrichtextfield.models import RichTextField


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    RichTextField = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('contributor_comment', 'date_of_comment', 'image', 'content', 'approved')
    RichTextField = ('content')

