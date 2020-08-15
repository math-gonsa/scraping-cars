from worker import items
from scrapy.loader import ItemLoader
import scrapy, random


class OLXSpider(scrapy.Spider):
    name = 'olx'

    def start_requests(self):
        states = ["ac","al","ap","am","ba","ce","df","es","go","ma","mt","ms","mg","pa","pb","pr","pe","pi","rj","rn","rs","ro","rr","sc","sp","se","to"]
        url = f"https://{random.choice(states)}.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios"
        yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li/a')
        for item in items:
            url = item.xpath('./@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        
        next_page = response.xpath('//a[@data-lurker-detail="next_page"]/@href').extract_first()
        print(next_page)
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
    
    def parse_detail(self, response):
        loader = ItemLoader(items.Car(), response=response)
        loader.add_value("url", response.url)
        loader.add_xpath("price", '//h2[@class="sc-ifAKCX sc-1leoitd-0 buyYie"]/text()')
        loader.add_xpath("model", '//span[text()="Modelo"]/following-sibling::a/text()')
        loader.add_xpath("brand", '//span[text()="Marca"]/following-sibling::a/text()')
        loader.add_xpath("type_vehicle", '//span[text()="Tipo de veículo"]/following-sibling::span/text()')
        loader.add_xpath("year_manufacture", '//span[text()="Ano"]/following-sibling::a/text()')
        loader.add_xpath("milage", '//span[text()="Quilometragem"]/following-sibling::span/text()')
        loader.add_xpath("type_fuel", '//span[text()="Combustível"]/following-sibling::a/text()')
        loader.add_xpath("type_shift", '//span[text()="Câmbio"]/following-sibling::span/text()')
        loader.add_xpath("type_steering", '//span[text()="Direção"]/following-sibling::span/text()')
        loader.add_xpath("color", '//span[text()="Cor"]/following-sibling::span/text()')
        loader.add_xpath("motor_power", '//span[text()="Potência do motor"]/following-sibling::span/text()')
        loader.add_xpath("number_of_doors", '//span[text()="Portas"]/following-sibling::span/text()')
        loader.add_xpath("neighborhood", '//dt[text()="Bairro"]/following-sibling::dd/text()')
        loader.add_xpath("city", '//dt[text()="Município"]/following-sibling::dd/text()')
        yield loader.load_item()