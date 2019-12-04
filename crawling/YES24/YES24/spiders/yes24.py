# -*- coding: utf-8 -*-
import scrapy


class Yes24Spider(scrapy.Spider):
    name = 'yes24'
    allowed_domains = ['www.yes24.com']
    start_urls = ['http://www.yes24.com/']

    def parse(self, response):
        print(response.text)
