import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://pl.wikipedia.org/wiki/Bumerang"]

    a = 0

    def parse(self, response):
        if self.a < 5:
            self.a += 1
            links = response.css(
                ".mw-parser-output > *:not(#Vorlage_Alternative):not(.metadata) a[href^='/wiki']::attr(href)"
            ).getall()
            links = [link for link in links if "." not in link]
            yield response.follow(links[0])
        else:
            yield {
                "url": response.url,
                "title": response.css(".mw-page-title-main::text").get(),
            }
