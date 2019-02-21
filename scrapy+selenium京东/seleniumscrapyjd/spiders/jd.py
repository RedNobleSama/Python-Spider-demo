# -*- coding: utf-8 -*-
import scrapy
from seleniumscrapyjd.items import JDProductItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    base_url = 'https://list.jd.com/list.html?cat=670,671,672'

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = self.base_url
            yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('.//div[@id="plist"]/ul[contains(@class, "gl-warp")]/li[@class="gl-item"]')
        for product in products:
            item = JDProductItem()
            item['title'] = product.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            item['image'] = 'http:' + product.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            item['price'] = product.xpath('.//div[@class="p-price"]/strong[@class="J_price"][1]/i/text()').extract_first()
            item['comments'] = product.xpath('.//a[@class="comment"]/text()').extract_first()
            item['shop'] = product.xpath('.//div[@class="p-shop"]/span/a/text()').extract_first()
            yield item