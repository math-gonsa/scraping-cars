from worker import items
from scrapy.loader import ItemLoader
import scrapy, json, random

class WebmotorsSpider(scrapy.Spider):
    name = 'webmotors'
    page_initial = random.randint(0, 15600)

    def start_requests(self):
        url = f"https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%3F&actualPage={str(self.page_initial)}&displayPerPage=48&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        
        for result in data['SearchResults']:
            yield scrapy.Request(url=f"https://www.webmotors.com.br/api/detail/car/{result['UniqueId']}", callback=self.parse_detail)           

        # if self.page_initial == None:
        #     self.page_initial = data['Count'] // len(data['SearchResults'])
        
        for i in range( (self.page_initial + 1), (self.page_initial + 50) ):
            url = f"https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros%2Festoque%3F&actualPage={str(i)}&displayPerPage=48&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false"
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse_detail(self, response):
        result = json.loads(response.body)

        loader = ItemLoader(items.Car(), response=response)

        url = f"https://www.webmotors.com.br/comprar/x/x/x/x/x/{str(result['UniqueId'])}"
        loader.add_value("url", url)
        
        price = str(result['Prices']['Price'])
        loader.add_value("price", price)
        
        model = result['Specification']['Title']
        loader.add_value("model", model)
        
        brand = result['Specification']['Make']['Value']
        loader.add_value("brand", brand)
        
        type_vehicle = result['Specification']['BodyType']
        loader.add_value("type_vehicle", type_vehicle)
        
        year_manufacture = result['Specification']['YearFabrication']
        loader.add_value("year_manufacture", year_manufacture)
        
        milage = result['Specification']['Odometer']
        loader.add_value("milage", milage)
    
        type_fuel = "Flex" if result['Specification']['Fuel'] == 'Gasolina e álcool' else result['Specification']['Fuel']
        loader.add_value("type_fuel", '')
        
        type_shift = result['Specification']['Transmission']
        loader.add_value("type_shift", type_shift)
        
        loader.add_value("type_steering", '')
        
        color = result['Specification']['Color']['Primary']
        loader.add_value("color", color)
        
        loader.add_value("motor_power", '')
        
        number_of_doors = result['Specification']['NumberPorts']
        loader.add_value("number_of_doors", number_of_doors)

        loader.add_value("neighborhood", '')
        
        city = result['Seller']['City']
        loader.add_value("city", city)
        
        yield loader.load_item()