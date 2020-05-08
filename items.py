# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    film = scrapy.Field()
    date = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    rate = scrapy.Field()
"""
    film ismi : div title_wrapper h1 text
    filmin tarihi : div tittle_wrapper h1 span a text
    film ulkesi :div txt-block[1] h4 a text
    film yonetmen : div credit_summary_item a text
    oyuncular : div credit_summary_item a[2] -- tiklanildiginda ;
    table cast_list tbody td[1] a text
    rate : div ratingValue strong span text
    """



