# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings


class DouyuspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        imageUrl = item['imageUrl']
        yield scrapy.Request(imageUrl)

    def item_completed(self, results, item, info):
        print("results:",results)
        if results[0][0] == True:
            image_path = self.IMAGES_STORE +'/'+ results[0][1]['path']
            print('image_path:',image_path)
            new_image_path = self.IMAGES_STORE + "/" + item['nickname'] + ".jpg"
            print('new name:',new_image_path)
            os.rename(image_path,new_image_path)

        return item



