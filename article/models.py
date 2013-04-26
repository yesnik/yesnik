#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    tag_rus = models.CharField(max_length=100, verbose_name='Название тэга')
    tag_url = models.SlugField(unique=True)

    def __unicode__(self):
        return self.tag_rus

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    published = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

