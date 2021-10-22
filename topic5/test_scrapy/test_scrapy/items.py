# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_weather(value):
    return value[0].replace('-','-')


class CityWeather(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    weather = scrapy.Field(serialize=serialize_weather)
