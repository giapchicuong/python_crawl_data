# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    Link = scrapy.Field()
    BlogName =scrapy.Field()
    Author =scrapy.Field()
    Description =scrapy.Field()
    Title =scrapy.Field()
