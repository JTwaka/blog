#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from project.views import index, base, heartbeat, bug, question, wheelchair

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^base/$', base, name='base'),

]

urlpatterns += [
    url(r'^bug/$', bug, name='bug'),
    url(r'^heartbeat/$', heartbeat, name='heartbeat'),
    url(r'^question/$', question, name='question'),
    url(r'^wheelchair/$', wheelchair, name='wheelchair'),
]