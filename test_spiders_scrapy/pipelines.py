# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import requests

class TestSpidersScrapyPipeline(object):
    def process_item(self, item, spider):
        '''
        处理每一个从SZtianqi传过来的
        item
        '''

        with open('weather.txt', 'a+') as f:
            f.write('日期：{}，温度：{}，风：{}，图标：{},\n'.format(item['date'], item['temperature'], item['wind'], item['img']))

        return item
