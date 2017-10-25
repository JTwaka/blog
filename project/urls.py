#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from project.views import index, base, about, links, heartbeat, bug, wheelchair

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^base/$', base, name='base'),
    url(r'^about/$', about, name='about'),
    url(r'^links/$', links, name='links'),

]

urlpatterns += [
    url(r'^bug/$', bug, name='bug'),
    url(r'^heartbeat/$', heartbeat, name='heartbeat'),
    url(r'^wheelchair/$', wheelchair, name='wheelchair'),
]