from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from .models import Post, Comment, AddPost
# from .forms import CommentForm

# from django.contrib.auth.mixins import (
# UserPassesTestMixin, LoginRequiredMixin
# )

# # # Create your views here. / class based views


class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('date_of_post')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detailedpost.html'


class Comment(CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = '__all__'


# # LoginRequiredMixin,
class AddPost(CreateView):
    template_name = "addpost.html"
    model = AddPost
    fields = '__all__'
