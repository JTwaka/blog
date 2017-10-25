# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogModel(models.Model):
    """
    文章模型
    """
    content = models.TextField(verbose_name=u'内容')
    title = models.CharField(max_length=50, verbose_name=u'标题')

    class Meta:
        verbose_name_plural = verbose_name = u'成员退群消息'

