# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'jd'

    title = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    comments = scrapy.Field()
    shop = scrapy.Field()