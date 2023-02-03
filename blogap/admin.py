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
    list_display = (
        'contributor_comment', 'email', 'date_of_comment', 'image', 'content', 'approved'
        )
#     list_filter = ('approved', 'date_of_comment', 'contributor_comment')
#     search_fields = ('contributor_comment', 'email', 'content')
#     # search_fields = ('name')
#     RichTextField = ('content')
#     # action = ['approve_comments']

#     # def approve_comments(self, request, queryset):
#     #     queryset.update(approved=True)
#  contributor_comment = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name='comment')
#     email = models.EmailField()
#     date_of_comment = models.DateTimeField(auto_created=True)
#     image = CloudinaryField('image', default='placeholder')
#     content = RichTextField(max_length=7000, blank=True, null=True)
#     # content = models.TextField()
#     no_of_comments = models.ManyToManyField(User, related_name="blog_comment")
#     approved = models.BooleanField('Approved', default='False')
