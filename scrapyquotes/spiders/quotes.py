# -*- coding: utf-8 -*-
import scrapy
from scrapyquotes.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = QuotesItem()
            item['text'] = quote.xpath('./span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('./span/small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath('./div/meta/@content').extract_first()
            yield item

        next_url = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next_url)
        yield scrapy.Request(url=url, callback=self.parse)

        # quotes = response.css('.quote')
        # for quote in quotes:
        #     item = QuotesItem()
        #     item['text'] = quote.css('.text::text').extract_first()
        #     item['author'] = quote.css('.author::text').extract_first()
        #     item['tags'] = quote.css('.tags .tag::text').extract()
        #     yield item
