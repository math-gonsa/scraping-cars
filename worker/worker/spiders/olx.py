from worker import items
from scrapy.loader import ItemLoader
import scrapy

class OLXSpider(scrapy.Spider):
    name = 'olx'

    def start_requests(self):
        url = "https://pr.olx.com.br/regiao-de-foz-do-iguacu-e-cascavel/regiao-de-cascavel/autos-e-pecas/carros-vans-e-utilitarios"
        yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li/a')
        for item in items:
            url = item.xpath('./@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
                
    def parse_detail(self, response):
        doc = {}
        
        doc["url"] = response.url
        doc["price"] = response.xpath('//h2[@class="sc-ifAKCX sc-1leoitd-0 buyYie"]/text()').extract_first()
        doc["category"] = response.xpath('//span[text()="Categoria"]/following-sibling::a/text()').extract_first()
        doc["model"] = response.xpath('//span[text()="Modelo"]/following-sibling::a/text()').extract_first()
        doc["brand"] = response.xpath('//span[text()="Marca"]/following-sibling::a/text()').extract_first()
        doc["type_vehicle"] = response.xpath('//span[text()="Tipo de veículo"]/following-sibling::span/text()').extract_first()
        doc["year_manufacture"] = response.xpath('//span[text()="Ano"]/following-sibling::a/text()').extract_first()
        doc["milage"] = response.xpath('//span[text()="Quilometragem"]/following-sibling::span/text()').extract_first()
        doc["type_fuel"] = response.xpath('//span[text()="Combustível"]/following-sibling::a/text()').extract_first()
        doc["type_shift"] = response.xpath('//span[text()="Câmbio"]/following-sibling::span/text()').extract_first()
        doc["type_steering"] = response.xpath('//span[text()="Direção"]/following-sibling::span/text()').extract_first()
        doc["color"] = response.xpath('//span[text()="Cor"]/following-sibling::span/text()').extract_first()
        doc["motor_power"] = response.xpath('//span[text()="Potência do motor"]/following-sibling::span/text()').extract_first()
        doc["number_of_doors"] = response.xpath('//span[text()="Portas"]/following-sibling::span/text()').extract_first()
        yield doc