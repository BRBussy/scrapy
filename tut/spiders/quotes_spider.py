import scrapy


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
        for product in response.xpath('//div[contains(@class, "product")]'):
            print(product)
