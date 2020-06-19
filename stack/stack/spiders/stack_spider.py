from scrapy import Spider
from scrapy.selector import Selector

from stack.stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    custom_settings = {
        'CLOSESPIDER_TIMEOUT': 5,
        # 'ITEM_PIPELINES': {
        #    'stack.pipelines.StackPipeline': 300
        # } #    nechápu, proč takovéto rozdělení pipelines nefungovalo s Flaskem
    }

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')

        for q in questions:
            item = StackItem()
            item['title'] = q.xpath(
                'h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['link'] = q.xpath(
                'h3/a[@class="question-hyperlink"]/@href').extract()[0]
            item['question_teaser'] = q.xpath(
                'div[@class="excerpt"]/text()').extract()[0]
            item['user'] = q.xpath(
                'div[@class="started fr"]/div/div[@class="user-details"]/a/text()').extract()[0]
            item['created'] = q.xpath(
                'div[@class="started fr"]/div/div[@class="user-action-time"]/span/text()').extract()[0]
            item['time'] = q.xpath(
                'div[@class="started fr"]/div/div[@class="user-action-time"]/span/@title').extract()[0]

            yield item



