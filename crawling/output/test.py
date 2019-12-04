# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09&year=2008&month=2&FetchSize=80', 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001/']

    def parse(self, response):
        print(response.text)
        
