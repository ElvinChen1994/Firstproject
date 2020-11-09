"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.http import HttpResponse
from book.views import book,book_detail,art_detail,publicer_detail
from movie.views import movie
from django.urls import converters    #转换器

def index(request):
    return  HttpResponse("首页")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('book/',include('book.urls')),
   # path('book/detail/<book_id>', book_detail),
    path('movie/',movie)
    #path('book/details/',art_detail),
    #path('book/publicer/<uuid:publicer_id>',publicer_detail)
]
