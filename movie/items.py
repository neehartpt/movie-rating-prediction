# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieBudgetItem(scrapy.Item):
    num_rows = scrapy.Field()
    release_date = scrapy.Field()
    movie_link = scrapy.Field()
    movie_name = scrapy.Field()
    production_budget = scrapy.Field()
    domestic_gross = scrapy.Field()
    worldwide_gross = scrapy.Field() 

