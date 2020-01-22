# -*- coding: utf-8 -*-
import scrapy


class MovlistSpider(scrapy.Spider):
    name = 'movlist'
   # allowed_domains = ['http://b1g-arch1ve.buho.ch/techhouse/Electro%20House/']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        print(response)
              
        #print(response.headers)
