from django.contrib import admin
from .models import Post, Comment
from djrichtextfield.models import RichTextField
# from django.utils.text import slugify


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    RichTextField = ('content')
    prepopulated_fields = {'slug': ('name',)}
#     # search_fields = ('name')
#     # list_display = ('name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'contributor_comment', 'date_of_comment', 'image', 'content', 'approved'
        )
#     # search_fields = ('name')
#     RichTextField = ('content')
#     # action = ['approve_comments']

#     # def approve_comments(self, request, queryset):
#     #     queryset.update(approved=True)
