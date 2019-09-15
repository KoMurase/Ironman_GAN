import scrapy
from scrapy.spiders import CrawlSpider, Rule
from mycrawler.items import MycrawlerItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://www.kokoro-yuyu.com/entry/2016/08/12/210000']

    def parse(self, response):
        item = MycrawlerItem()
        item["image_urls"] = []
        for image_url in response.xpath("//img/@src").extract():
            if "http" not in image_url:
                item["image_urls"].append(response.url.rsplit("/", 1)[0] + "/" + image_url)
            else:
                item["image_urls"].append(image_url)

        return item
