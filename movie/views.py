# -*- coding: utf-8 -*-
# @Time : 2020/11/6 12:59 上午
# @Author : Elvin
# @Email : 1203456820@qq.com
# @File : views.py
# @Project : firstproject
from django.http import HttpResponse


def movie(request):
    return  HttpResponse("see you")