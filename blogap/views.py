from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Post, Comment
from django.http import HttpResponse

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


class Comment(generic.FormView):
    model = Comment
    template_name = 'comment.html'



        





# # class AddPost(LoginRequiredMixin, AddPost):
# #     template_name = "addpost.html"
# #     model = AddPost
# #     # form_class = AddPostForm
# #     success_url = '/'

    # #     def form_valid(self, form):
# #         form.instance.user = self.request.user
# #         return super(AddPost, self).form_valid(form)






