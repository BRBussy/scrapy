import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = ['https://www.biltongandbudz.co.za/shop/']
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                cookies={'age_gate': 21, 'tk_ai': 'woo:dBlQRi3iIybLcJZIZaok+wyL'}
            )

    def parse(self, response):
        product_links = set()

        for item in response.xpath('//div[@class="shop-container"]/div[contains(@class, "products")]/div'):
            for link in Selector(text=item.extract()).xpath('//a/@href'):
                link_text = link.extract()
                if 'http' in link_text and 'product' in link_text:
                    product_links.add(link.extract())

        for link in product_links:
            yield scrapy.Request(
                url=link,
                callback=self.process_product_page,
                cookies={'age_gate': 21, 'tk_ai': 'woo:dBlQRi3iIybLcJZIZaok+wyL'}
            )

    def process_product_page(self, response):
        print('process page!', response.url)
