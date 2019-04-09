# -*- coding: utf-8 -*-
import scrapy
import re
from shopSpider.items import ShopspiderItem

class Shopping2Spider(scrapy.Spider):
    name = 'shopping2'
    allowed_domains = ['tejia.aili.com']
    start_urls = ['http://tejia.aili.com/index_1.html']

    def __init__(self):
        self.page = 1
        self.maxpage = 20
        self.str1 = "http://tejia.aili.com/index_"
        self.str2 = ".html"

    def get_url(self):
        return self.str1 + str(self.page) + self.str2

    def parse(self, response):
        ls = response.xpath('//div[@class="prl list_li indx_li"]')
        print(len(ls))
        for item in ls:
            name = item.xpath('./div[@class="p_name"]//span/text()').extract()[0]
            print("商品名：", name)
            url = item.xpath('./div[@class="p_img"]/a/@href').extract()[0]
            print("链接：", url)
            price = item.xpath('./div[@class="p_pg"]/span/text()').extract()[0]
            print("价格：", price)

            "准备进入pipelines存入数据"
            item = ShopspiderItem()
            item['name'] = name
            item['url'] = url
            item['price'] = price
            yield item

        "设置翻页"
        cur_url = response.url
        # print(cur_url)
        p = self.str1 + r'(\d+).*?'
        page = re.search(p, cur_url)
        cur_page =page.group(1)
        print("当前页数：", cur_page)
        self.page = int(cur_page) + 1
        if int(cur_page) <= self.maxpage:
            url = self.get_url()
            "封装一个请求对象放入请求等待队列,第一个参数url,第二个参数解析"
            yield scrapy.Request(url, callback=self.parse)


