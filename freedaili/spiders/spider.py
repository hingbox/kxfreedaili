# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from freedaili.items import FreedailiItem
add=0
class FreeDaiLiSpider(CrawlSpider):
    name="freedaili"
    allowed_domains = ["www.kuaidaili.com"]
    start_urls = ['http://www.kuaidaili.com/free/inha/']
    # def parse(self, response):
    #     items =[]
    #     item = FreedailiItem()
    #     #ip = response.xpath('//div[@id="list"]/table/tbody/tr/')
    #     contents =response.xpath("//tr")
    #     for content in contents:
    #         tds= content.xpath('./td/text()').extract()
    #         item['content']=tds
    #         yield item


    rules = (
            Rule(LinkExtractor(allow=('/*',)), callback='parse_item', follow=True),
            # Rule(LinkExtractor(allow=('intr/*',)), callback='parse_item', follow=True),
            # Rule(LinkExtractor(allow=('outha/*',)), callback='parse_item', follow=True),
            # Rule(LinkExtractor(allow=('outtr/*',)), callback='parse_item', follow=True),
        )

    def parse_item(self,response):

        item = FreedailiItem()
        contents = response.xpath("//tr")
        for content in contents:
            tds= content.xpath('./td/text()').extract()
            item['content']=tds
            yield item

