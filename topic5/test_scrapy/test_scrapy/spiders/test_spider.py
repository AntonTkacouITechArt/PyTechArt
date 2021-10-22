import scrapy
from test_scrapy.items import CityWeather

class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['yandex.by']
    start_urls = ['https://yandex.by/pogoda/region/149',]

    # def start_requests(self):


    def parse_city_url(self, response, **kwargs):
        urls = response.css('.place-list__item-name::attr(href)').extract()
        names = response.css('.place-list__item-name::text').extract()
        rows_data = list(zip(names, urls))
        data = []
        for row in rows_data:
            if row[0] != 'Беларусь':
                url = 'https://yandex.by/pogoda'+ row[1]
                city = row[0]
                data.append({'url':url,'city':city})
        yield data


    def parse(self, response):
        names = response.css('.place-list__item-name::text').extract()
        links = response.css('.place-list__item-name::attr(href)').extract()
        data = list(zip(links, names))
        for col in data:
            if col[1] != 'Беларусь': 
                url = 'https://yandex.by' + col[0]
                name = col[1]
                yield scrapy.Request(url,callback = self.parse_weather, meta={'name': name})

    def parse_weather(self, response):
        temperature = response.xpath(
            '//div[contains(@class, "temp fact__temp")]/span[contains(@class,"temp__value")]/text()').extract()
        item = CityWeather()
        item['city'] = response.meta.get('name')
        item['weather'] = temperature
        yield item


