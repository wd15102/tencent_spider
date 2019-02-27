# -*- coding: utf-8 -*-
import scrapy
from pachong.items import PachongItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]
    def parse(self, response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = PachongItem()
            item['positionName']= each.xpath('.//td[1]/a/text()').extract_first()
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract_first()
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract_first()
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract_first()
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract_first()
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract_first()
            if self.offset <2910:
                self.offset+=10
            #回调函数继续请求后面所有页面数据
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
            yield item