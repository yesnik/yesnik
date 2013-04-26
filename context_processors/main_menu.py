#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from article.models import Tag

def main_menu(request):
    tag_list = Tag.objects.all()
    return {'var1':'This is var 1 from Context Processor!',
            'var2':'This is var 2 from Context Processor!',
            'tag_list': tag_list}