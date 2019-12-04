import os
from time import sleep

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

year = 2019


class Yes24Spider(scrapy.Spider):
    name = 'yes24'
    start_urls = [
        f'http://www.yes24.com/24/category/bestseller?sumgb=09&year={year}&month={month}&FetchSize=80'
        for month in range(12, 12+1)

        #for year in years
    ]

    def parse(self, response):
        for item in response.css('.goodsTxtInfo p:first-child'):
            url = item.css('a:first-child::attr(href)').get()
            title = ''.join(item.css('::text').extract()).strip()
            print(url, title)
            yield response.follow(url, self.parse_detail)

    def parse_detail(self, response):
        sleep(1)
        title = response.css('.gd_name::text').get()
        if not title:
            return
        yield {
            'title': title.strip(),
            'title2': (response.css('.gd_nameE::text').get() or '').strip(),
            'rating': response.css('.gd_rating:first-child .yes_b::text').get(),
            'tags': ','.join(response.css('.tagArea .tag a::text').extract())
        }


if __name__ == '__main__':
    os.system('rm ./output/items_201911.csv')
    process = CrawlerProcess({
        **get_project_settings(),
        'FEED_FORMAT': 'CSV',
        'FEED_URI': 'output/items_201911.csv'
    })
    process.crawl(Yes24Spider)
    process.start()
