from django.contrib import admin
from .models import Post, Comment
#  AddComment
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
    def __str__(self):
        return f"{self.title} {self.contributor_comment}"
    # list_display = ('title', 'contributor_comment')
   
    # pass
