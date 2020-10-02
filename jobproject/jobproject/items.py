# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# 引入django中app中models文件中的类
from app51.models import app51data
# scrapy与django对接的库
from scrapy_djangoitem import DjangoItem


class JobprojectItem(DjangoItem):
    django_model = app51data


