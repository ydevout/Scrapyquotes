# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class QuotesItem(Item):
    # collection = 'quotes'
    text = Field()
    author = Field()
    tags = Field()
