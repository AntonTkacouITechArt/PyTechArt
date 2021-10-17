import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['yandex.by']
    start_urls = ['http://yandex.by/pogoda/region/149/']

    def parse(self, response):
        star_rating = response
        data = []
        for href in response.xpath("//li[@class='Region_elem__3UQmE']/a/@href"):
            print(href)
            data.append(href
                        )
        pass
