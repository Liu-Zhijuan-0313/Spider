# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from shopSpider.items import ShopspiderItem


class ShoppingSpider(CrawlSpider):
    name = 'shopping'
    allowed_domains = ['tejia.aili.com']
    start_urls = ['http://tejia.aili.com/index.html']
    # pagelink = LinkExtractor(restrict_xpaths=('//a[@id="next-page"]'))
    pagelink = LinkExtractor(restrict_css=('a[id="next-page"]'))
    rules = [
        Rule(pagelink, callback="parse_item", follow=True)
    ]

    def parse_item(self, response):

        ls = response.xpath('//div[@class="prl list_li indx_li"]')
        print(len(ls))
        for item in ls:
            name = item.xpath('./div[@class="p_name"]//span/text()').extract()[0]
            print("商品名：", name)
            url = item.xpath('./div[@class="p_img"]/a/@href').extract()[0]
            print("链接：", url)
            price = item.xpath('./div[@class="p_pg"]/span/text()').extract()[0]
            print("价格：", price)

            item = ShopspiderItem()
            item['name'] = name
            item['url'] = url
            item['price'] = price
            yield item
