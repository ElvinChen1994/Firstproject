# -*- coding: utf-8 -*-
# @Time : 2020/11/6 12:57 上午
# @Author : Elvin
# @Email : 1203456820@qq.com
# @File : views.py
# @Project : firstproject

from django.http import HttpResponse


def book(request):

    return  HttpResponse("i love you")

def book_detail(request, book_id):
    #可以从数据库中根据book_id提取这个图书信息
    text = "输入的图书ID是： %s" % book_id
    return HttpResponse(text)

def art_detail(request):
    art_id = request.GET.get('id')
    #rt_id = request.GET['id']
    text = '我的id是：%s' % art_id
    return HttpResponse(text)

def publicer_detail(request, publicer_id):
    text = '你的id是：%s' % publicer_id
    return HttpResponse(text)