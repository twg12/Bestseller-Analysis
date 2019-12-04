# -*- coding: utf-8 -*-
import scrapy


class Yes24bsSpider(scrapy.Spider):
    name = 'yes24bs'
    allowed_domains = ['http://www.yes24.com/24/category/bestseller?CategoryNumber=001']
    start_urls = ['http://http://www.yes24.com/24/category/bestseller?CategoryNumber=001/']

    def parse(self, response):
        pass
