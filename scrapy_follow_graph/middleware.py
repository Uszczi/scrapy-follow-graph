from scrapy.http import Request


class FollowGraphMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_spider_output(self, response, result, spider):
        self._init_follow(response, spider)
        return (r for r in result or () if self._filter(r, response, spider))

    async def process_spider_output_async(self, response, result, spider):
        self._init_follow(response, spider)
        async for r in result or ():
            if self._filter(r, response, spider):
                yield r

    def _init_follow(self, response, spider):
        if "scrapy_follow_path" not in response.meta:
            response.meta["scrapy_follow_path"] = []

    def _filter(self, request, response, spider):
        scrapy_follow_path = response.meta["scrapy_follow_path"]

        if isinstance(request, Request):
            scrapy_follow_path.append(response.url)
            request.meta["scrapy_follow_path"] = scrapy_follow_path
        else:
            scrapy_follow_path.extend([response.url])
            scrapy_follow_path.append(request["title"])
            request["scrapy_follow_path"] = scrapy_follow_path
        return True
