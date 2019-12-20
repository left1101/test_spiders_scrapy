# -*- coding: utf-8 -*-
import scrapy
from test_spiders_scrapy.items import TestSpidersScrapyItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['tianqi.com']

    def start_requests(self):
        headers = {
            'cookie': 'cityPy=beijing; cityPy_expire=1575895438; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1575290640; UM_distinctid=16ec6a3987d4f6-0570511e529788-3964720e-384000-16ec6a3987e2ed; CNZZDATA1277722738=1600153008-1575290479-null%7C1575290479; CNZZDATA1268732535=1876818844-1575286820-https%253A%252F%252Fwww.tianqi.com%252F%7C1575525307; CNZZDATA1275796416=684916782-1575285602-%7C1575528968; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1575529280',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        citys = ['beijing', 'shanghai', 'fuzhou', 'xiamen', 'shunchang', 'nanping']
        urls = []
        for city in citys:
            urls.append('http://www.tianqi.com/' + city + '/30/')

        for url in urls:
            yield scrapy.Request(url, headers=headers)


    def parse(self, response):
        '''
        筛选信息的函数：
        date = 今日日期
        week = 星期几
        img = 表示天气的图标
        temperature = 当天的温度
        weather = 当天的天气
        wind = 当天的风向
        '''
        items = []

        days1 = response.xpath('//div[@class="box_day"]/div[@class="table_day tbg"]')
        days2 = response.xpath('//div[@class="box_day"]/div[@class="table_day "]')
        days = days1 + days2

        for idx, day in enumerate(days):
            item = TestSpidersScrapyItem()

            if idx <= 6:
                item['date'] = ''.join(day.xpath('./a/h3//text()').extract())
                item['img'] = day.xpath('./a/ul/li[@class="img"]/img/@src').extract()[0]
                td = day.xpath('./a/ul/li[@class="temp"]//text()').extract()
                item['temperature'] = ''.join(td)
                item['wind'] = day.xpath('./a/ul/li[3]//text()').extract()[0]
            else:
                item['date'] = ''.join(day.xpath('./h3//text()').extract())
                item['img'] = day.xpath('./ul/li[@class="img"]/img/@src').extract()[0]
                td = day.xpath('./ul/li[@class="temp"]//text()').extract()
                item['temperature'] = ''.join(td)
                item['wind'] = day.xpath('./ul/li[3]//text()').extract()[0]

            items.append(item)

        return items
