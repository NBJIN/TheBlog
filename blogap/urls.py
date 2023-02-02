
from . import views
# from django.contrib import admin
from django.urls import path, include
from .views import PostView, PostDetail, Comment


urlpatterns = [

#     path('', views.index, name="index.html"),
#     # # path('djrichtextfield/', include('djrichtextfield.urls')),
#     # # path('<slug:slug>/', views.addpost, name='addpost'),
#     # # path('', views.index, name=index)
    path('', views.PostView.as_view(), name='index'),
    # path('Comment/', views.Comment.as_view(), name='comment')
    # path('', include('blogap.urls'), name='blogap'),
    # path('<slug:slug>/', views.PostDetailView(), name='detailpost'),
    # 'article/<int:pk>'
    path('detailed_post/<int:pk>', PostDetail.as_view(), name='detailed_post'),
    # path('comment/<slug:contributor_comment>', Comment.as_view(), name='comment')
    path('comment/', views.Comment.as_view(), name='comment'),
]
