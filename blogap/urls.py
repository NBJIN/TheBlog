from django.urls import path
from . import views

urlpatterns = [
    path('', view.PostList.as_view(), name='home')
]