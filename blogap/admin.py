from django.contrib import admin
from .models import Post, Comment
#  AddComment
from djrichtextfield.models import RichTextField

# from django.utils.text import slugify


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    RichTextField = ('content')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'date_of_post')
    list_display = ('name', 'slug', 'post_contributor', 'date_of_post') # not sure about this line
    search_fields = ('name', 'content')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('contributor_comment', 'date_of_comment', 'content', 'approved')
    list_filter = ('contributor_comment', 'date_of_comment')
    search_fields = ('contributor_comment', 'date_of_comment', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    # def __str__(self):
    #     return f"{self.title} {self.contributor_comment}"
 