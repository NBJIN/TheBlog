from . import views
# from django.contrib import admin
from django.urls import path, include


urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', include('blogap.urls')),
#     path('', views.index, name="index.html"),
#     # # path('djrichtextfield/', include('djrichtextfield.urls')),
#     # # path('<slug:slug>/', views.addpost, name='addpost'),
#     # # path('', views.index, name=index)
    path('', views.PostList.as_view(), name='index'),
    # path('Comment/', views.Comment.as_view(), name='comment')
    

 
 

]
