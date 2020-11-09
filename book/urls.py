# -*- coding: utf-8 -*-
# @Time : 2020/11/7 3:30 下午
# @Author : Elvin
# @Email : 1203456820@qq.com
# @File : urls.py
# @Project : firstproject
from django.urls import path
from book import views
urlpatterns = [
    path('', views.book),
    path('detail/<book_id>/', views.book_detail),

]