# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jdbook1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    first_catalog = scrapy.Field()
    second_catalog = scrapy.Field()

    book_name = scrapy.Field()
    picture_url = scrapy.Field()
    book_author = scrapy.Field()
    publish_house = scrapy.Field()
    publish_time = scrapy.Field()
    book_price = scrapy.Field()

