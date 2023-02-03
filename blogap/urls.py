from . import views
# from django.contrib import admin
from django.urls import path, include
from .views import PostView, PostDetail, Comment
from django.http import HttpResponse


urlpatterns = [
        path('', views.PostView.as_view(), name='index'),
        path('detailedpost/<int:pk>', views.PostDetail.as_view(), name='detailedpost'),
        path('<int:pk>/comment', views.Comment.as_view(), name='comment'),

]
#     path('', views.index, name="index.html"),
#     # # path('djrichtextfield/', include('djrichtextfield.urls')),
#     # # path('<slug:slug>/', views.addpost, name='addpost'),
#     # # path('', views.index, name=index)
   
    # path('Comment/', views.Comment.as_view(), name='comment')
    # path('', include('blogap.urls'), name='blogap'),
    # path('<slug:slug>/', views.PostDetailView(), name='detailpost'),
    # 'article/<int:pk>'
    # 
    # path('comment/<slug:contributor_comment>', Comment.as_view(), name='comment')
#     path('addcomment/<int:pk>', views.AddComment.as_view(), name='addcomment'),