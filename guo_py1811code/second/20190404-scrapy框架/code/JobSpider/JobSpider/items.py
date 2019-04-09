# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称，招聘公司，工作城市，薪资，发布时间
    name = scrapy.Field()
    corp = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    pub_date = scrapy.Field()

