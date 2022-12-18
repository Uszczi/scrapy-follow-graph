import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['wikipedia.com']
    start_urls = ['http://wikipedia.com/']

    def parse(self, response):
        pass
