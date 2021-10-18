# -*- coding: utf-8 -*-
import scrapy
import csv


class GetWeatherSpider(scrapy.Spider):
    name = 'get_weather'
    allowed_domains = ['yandex.by']
    csvfile = open('City_URL.csv', 'r', newline='')
    reader = csv.DictReader(csvfile)
    urls = []
    names = []
    for row in reader:
        urls.append(row['URL'])
        names.append(row['City'])
    start_urls = urls
    csvfile.close()

    def __init__(self):
        self.outfile = open('City_Weather.csv', 'w', newline='')
        self.writer = csv.writer(self.outfile)
        self.writer.writerow(['City', 'Weather'])

    def closed(self, reason):
        self.outfile.close()

    def parse(self, response):
        # tag from link below
        # https://yandex.by/pogoda/baranavichy?via=reg
        temperatura = response.xpath('//div[@class="temp fact__temp fact__temp_size_s"]/span[@class="temp__value temp__value_with-unit"/text()]').extract()
        print(temperatura)
        result = list(zip(GetWeatherSpider.names, temperatura))
        print(result)
        for row in result:
            scraped_info = {
                row[0]: row[1],
            }
            self.writer.writerow([row[0], row[1]])
            yield scraped_info
