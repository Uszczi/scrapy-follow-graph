import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://pl.wikipedia.org/wiki/Bumerang",
        "https://en.wikipedia.org/wiki/The_Witcher",
    ]
    custom_settings = {
        "SPIDER_MIDDLEWARES": {
            "scrapy_follow_graph.middleware.FollowGraphMiddleware": 543,
        },
    }

    links_selector = (
        ".mw-parser-output > "
        "*:not(#Vorlage_Alternative):not(.metadata) "
        "a[href^='/wiki']:not([href*='jpg']):not(.mw-disambig)::attr(href)"
    )

    def parse(self, response):
        if response.meta["depth"] < 5:
            links = response.css(self.links_selector).getall()
            links = [link for link in links if "." not in link]
            yield response.follow(links[0])
        else:
            yield {
                "url": response.url,
                "title": response.css(".mw-page-title-main::text").get(),
            }
