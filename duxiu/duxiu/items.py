# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DuxiuItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    subtype = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date_of_pub = scrapy.Field()
    pages = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()