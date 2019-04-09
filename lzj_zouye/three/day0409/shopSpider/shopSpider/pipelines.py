# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


"""
1.存入CSV中
"""

import csv
import codecs


class ShopspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open("shopping.csv", "w", "utf-8")
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name', 'url', 'price'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['url'], item['price']])
        return item

    def close(self):
        self.file.close()


"""
2.存入数据库中
"""


import pymysql


# class ShopspiderPipeline(object):
#     def __init__(self):
#         self.con = pymysql.Connect(user="root", password="123456",
#                  database="goods")
#         self.cur = self.con.cursor()
#
#     def process_item(self, item, spider):
#         sql = "insert into shopping values(0, %s, %s, %s)"
#         params = [item['name'], item['url'], item['price']]
#         self.cur.execute(sql, params)
#         self.con.commit()
#         return item
#
#     def close(self):
#         self.con.close()
#         self.cur.close()
