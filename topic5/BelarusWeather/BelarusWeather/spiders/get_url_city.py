# -*- coding: utf-8 -*-
import scrapy, csv


class GetUrlCitySpider(scrapy.Spider):
    name = 'get_url_city'
    allowed_domains = ['yandex.by']
    start_urls = ['https://yandex.by/pogoda/region/149/']

    # custom_settings = {
    #     'FEED_URI': 'Cities_and_URLS.csv'
    # }

    def __init__(self):
        self.outfile = open('City_URL.csv', 'w', newline='')
        self.writer = csv.writer(self.outfile)
        self.writer.writerow(['City', 'URL'])

    def closed(self, reason):
        self.outfile.close()

    def parse(self, response):
        print('Start processing response:' + response.url)
        print('Example name city:' + response.css(
            '.place-list__item-name').extract_first())
        print('Example url city' + response.css(
            '.place-list__item-name::attr(href)').extract_first())
        names = response.css('.place-list__item-name::text').extract()
        urls = response.css('.place-list__item-name::attr(href)').extract()
        rows_data = list(zip(names, urls))
        for row in rows_data:
            scraped_info = {
                row[0]: 'https://yandex.by/pogoda' + row[1],
            }
            self.writer.writerow([row[0], 'https://yandex.by' + row[1]])
            yield scraped_info
