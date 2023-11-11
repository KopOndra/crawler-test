import math
import time
import json

import scrapy
from sreality_crawler.items import SrealityCrawlerItem


class FlatsSpider(scrapy.Spider):
    """Takes care of generating page urls and parsing needed data from it."""

    name = "flats"
    allowed_domains = ["www.sreality.cz"]
    start_urls = ["https://www.sreality.cz/hledani/prodej/byty"]
    pipeline = "sreality_crawler.pipelines.SrealityCrawlerPipeline"

    def parse(self, response):
        """Parse the page for the needed data."""
        jsonresponse = json.loads(response.text)
        items = jsonresponse["_embedded"]["estates"]
        for item in items:
            name = item["name"]
            url = item["_links"]["images"][0]["href"]
            flat_item = SrealityCrawlerItem(name=name, url=url)
            yield flat_item

    def start_requests(self):
        """Generate the urls we want to scrape."""
        time_stamp = int(math.floor(time.time()))
        urls = [
            scrapy.Request(
                url=f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page={i}&per_page=20&tms={time_stamp}/",
                dont_filter=True,
            )
            for i in range(1, 26)
        ]
        return urls
