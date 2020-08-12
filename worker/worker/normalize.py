from hashlib import md5
from datetime import datetime

def normalize_item(item):
    item['url_hash'] = generate_hash(item['url'])
    item['created_at'] = datetime.now()
    item = process_price(item)
    item = process_integer_fields(item)
    return item

def generate_hash(value):
    return md5(value.encode('utf-8')).hexdigest()

def process_price(item):
    if 'price' in item and item['price'] != None:
        for unnecessary in [ "R$", ".", "," ]:
            item['price'] = item['price'].replace(unnecessary, "")
        item['price'] = float(item['price'])
    return item

def process_integer_fields(item):
    fields = [ 'year_manufacture', 'milage' ]
    for field in fields:
        try:
            item[field] = int(item[field])
        except Exception as e: 
            pass
    return item