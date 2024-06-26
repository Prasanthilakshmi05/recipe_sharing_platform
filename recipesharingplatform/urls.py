"""
URL configuration for recipesharingplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .views import index
from .views import AllRecipes
from .views import Cookpad
from .views import Tasty
from .views import Yummly
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'index'),
    path('AllRecipes/',AllRecipes,name='AllRecipes'),
    path('Cookpad/',Cookpad,name='Cookpad'),
    path('Tasty/',Tasty,name='Tasty'),
    path('Yummly/',Yummly,name='Yummly'),
    path('accounts/', include('accounts.urls')),
    path('forms/', views.forms, name='forms'),
     path('AllRecipes/', include('AllRecipes.urls')),
]
