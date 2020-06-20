from scrapy import Spider
from scrapy.selector import Selector

from stack.stack.items import TagItem


# Pavouk, který se stará o tagy pod otázkama
class TagSpider(Spider):
    name = "tag"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    custom_settings = {
        'CLOSESPIDER_TIMEOUT': 5,
        # 'ITEM_PIPELINES': {
        #    'stack.pipelines.TagPipeline': 300
        # }  # nechápu, proč takovéto rozdělení pipelines nefungovalo s Flaskem

    }

    def parse(self, response):
        tags = Selector(response).xpath('//a[@class="post-tag"]')

        for t in tags:
            item = TagItem()
            item['name'] = t.xpath(
                'text()').extract()[0]
            # if len(item['name']) > 15:
            #     yield item              
            yield item  # Vrátí všechny tagy v posledních 50ti otázkách
