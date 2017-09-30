#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from project.views import index

urlpatterns = [
    url(r'', index, name='index'),
]