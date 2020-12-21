from worker import items
from scrapy.loader import ItemLoader
import scrapy, random


class MercadoLivreSpider(scrapy.Spider):
    name = 'mercadolivre'
    custom_settings = { 'CONCURRENT_REQUESTS': 4, 'DOWNLOAD_DELAY': 1 }
    def start_requests(self):
        url = "https://lista.mercadolivre.com.br/veiculos/"
        yield scrapy.Request(url=url, callback=self.parse )  #={"proxy": "http://104.131.17.56:80"})
            
    def parse(self, response):
        items = response.xpath('//li[@class="ui-search-layout__item"]')
        for item in items:
            url = item.xpath('./div/div/div/a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        
        next_page = response.xpath('//li[@class="andes-pagination__button andes-pagination__button--next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse )  #={"proxy": "http://104.131.17.56:80"})
    
    def parse_detail(self, response):
        loader = ItemLoader(items.Car(), response=response)
        loader.add_value("url", response.url)
        loader.add_xpath("price", '//span[@class="price-tag-fraction"]/text()')
        loader.add_xpath("model", '//tr[th[text()="Marca"]]/td/span/text()')
        loader.add_xpath("brand", '//tr[th[text()="Modelo"]]/td/span/text()')
        loader.add_xpath("type_vehicle", '//tr[th[text()="Tipo de carroceria"]]/td/span/text()')
        loader.add_xpath("year_manufacture", "//tr[th[text()='Ano']]/td/span/text()")
        loader.add_xpath("milage", '//tr[th[text()="Quilômetros"]]/td/span/text()', re=r'(.*)km')
        loader.add_xpath("type_fuel", '//tr[th[text()="Tipo de combustível"]]/td/span/text()')
        loader.add_xpath("type_shift", '//tr[th[text()="Transmissão"]]/td/span/text()')
        loader.add_xpath("type_steering", '//p[span[text()="Direção"]]/text()[2]')
        loader.add_xpath("color", '//tr[th[text()="Cor"]]/td/span/text()')
        loader.add_xpath("motor_power", '//tr[th[text()="Motor"]]/td/span/text()')
        loader.add_xpath("number_of_doors", '//tr[th[text()="Portas"]]/td/span/text()')
        loader.add_xpath("neighborhood", '//h3[text()="Localização do veículo"]/following-sibling::p/text()', re=r'(.*?) - .*')
        loader.add_xpath("city", '//h3[text()="Localização do veículo"]/following-sibling::p/text()', re=r'.*? - (.*?) -')
        yield loader.load_item()