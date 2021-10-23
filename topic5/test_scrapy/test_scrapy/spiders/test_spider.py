import scrapy
from scrapy.loader import ItemLoader
from test_scrapy.items import CityWeather

class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['yandex.by']
    start_urls = ['https://yandex.by/pogoda/region/149',]

    def parse(self, response):
        yield  from (response.follow(url.xpath('@href').get(),
                                     callback=self.parse_weather) 
                     for url in response.css('.place-list__item-name') 
                     if 'Беларусь' != url.xpath('text()'))

    def parse_weather(self, response):
        item = ItemLoader(item = CityWeather(), response = response)
        item.add_xpath('city', """//li[contains(@class, "breadcrumbs__item")]
        /span[contains(@class, "breadcrumbs__title")]/text()""")
        item.add_xpath('weather', """//div[contains(@class, "temp fact__temp")
        ]/span[contains(@class,"temp__value")]/text()""")
        yield item.load_item()


