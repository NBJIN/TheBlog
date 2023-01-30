from django.contrib import admin
from .models import Post
from djrichtextfield.models import RichTextField


@admin.register(Post)
class PostAdmin(RichTextField):

    RichTextField = ('content')
