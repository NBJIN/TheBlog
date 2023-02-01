"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from blogap import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blogap.urls')),
    # path('', views.index, name="index.html"),
    # path('djrichtextfield/', include('djrichtextfield.urls')),
    # path('<slug:slug>/', views.addpost, name='addpost'),
    # path('', views.index, name=index)
    path('', include('blogap.urls'), name='blogap'),
    

]
