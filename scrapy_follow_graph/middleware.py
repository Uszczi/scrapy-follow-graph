import json
from scrapy.http import Request
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
import os


class FollowGraphMiddleware:
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        print("[")
        print("[")
        print("[")
        print("[")
        print("[")
        crawler.signals.connect(cls._item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(cls._spider_closed, signal=signals.spider_closed)
        cls.file = open(
            "/home/mateusz/projects/scrapy-follow-graph/example_spider/asdf.json", "w"
        )
        cls.exporter = _JsonLinesItemExporter(cls.file)

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

    @classmethod
    def _item_scraped(cls, item):
        cls.exporter.export_item(item)
        print("asdfasdf")

    @classmethod
    def _spider_closed(cls):
        cls.exporter.finish_exporting()
        cls.file.close()
        print("]")
        print("]")
        print("]")
        print("]")
        print("]")


class _JsonLinesItemExporter:
    def __init__(self, file, **kwargs):
        self.file = file
        self.file.write("[\n")

    def export_item(self, item):
        data = json.dumps(item) + ",\n"
        self.file.write(data)

    def finish_exporting(self):
        self.file.seek(self.file.tell() - 2, os.SEEK_SET)
        self.file.write("\n]")
