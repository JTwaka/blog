
# -*- coding: utf-8 -*-
# //                            _ooOoo_
# //                           o8888888o
# //                           88" . "88
# //                           (| -_- |)
# //                           O\  =  /O
# //                        ____/`---'\____
# //                      .'  \\|     |//  `.
# //                     /  \\|||  :  |||//  \
# //                    /  _||||| -:- |||||-  \
# //                    |   | \\\  -  /// |   |
# //                    | \_|  ''\---/''  |   |
# //                    \  .-\__  `-`  ___/-. /
# //                  ___`. .'  /--.--\  `. . __
# //               ."" '<  `.___\_<|>_/___.'  >'"".
# //              | | :  `- \`.;`\ _ /`;.`/ - ` : | |
# //              \  \ `-.   \_ __\ /__ _/   .-` /  /
# //         ======`-.____`-.___\_____/___.-`____.-'======
# //                            `=---='
# //        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# //                      佛祖保佑       永无BUG
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):

    list = [1,2,3,4,5,6,1,2,324,235,1]
    article_list = getPage(request, list)

    return render(request, 'index.html', locals())


# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 6)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


#
def base(request):
    return render(request, 'base.html', locals())


def bug(request):
    return render(request, 'funny/bug.html', locals())


def heartbeat(request):
    return render(request, 'funny/heartbeat.html', locals())


def wheelchair(request):
    return render(request, 'funny/wheelchair.html', locals())


def question(request):
    return render(request, 'funny/question.html', locals())


