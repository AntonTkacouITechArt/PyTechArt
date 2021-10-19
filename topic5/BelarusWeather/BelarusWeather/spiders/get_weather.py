# -*- coding: utf-8 -*-
import scrapy
import csv


class GetWeatherSpider(scrapy.Spider):
    name = 'get_weather'
    allowed_domains = ['yandex.by']
    reader = None
    urls = []
    names = []
    counter = 0
    with open('/home/anton/MyGit/PyTechArt/topic5/BelarusWeather/City_URL.csv',
              'r',
              newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            urls.append(row['URL'])
            names.append(row['City'])
    start_urls = urls

    def __init__(self):
        self.outfile = open('City_Weather.csv', 'w', newline='')
        self.writer = csv.writer(self.outfile)
        self.writer.writerow(['City', 'Weather'])

    def closed(self, reason):
        self.outfile.close()

    def parse(self, response):
        temperature = response.xpath(
            '//div[contains(@class, "temp fact__temp")]/span[contains(@class,"temp__value")]/text()').extract()
        for temp in temperature:
            scraped_info = {
                GetWeatherSpider.names[GetWeatherSpider.counter]: temp,
            }
            self.writer.writerow(
                [GetWeatherSpider.names[GetWeatherSpider.counter], temp])
            GetWeatherSpider.counter += 1
            yield scraped_info
