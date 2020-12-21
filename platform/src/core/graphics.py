
import statistics

doc = {}
brands = list(collection.distinct("brand"))
percent = 20

for brand in brands:
    doc[brand] = counts( {"brand": brand} )

mean = statistics.mean(doc.values())
_max = mean + ( mean * ( percent / 100 ) )
_min = mean - ( mean * ( percent / 100 ) )

labels, sizes, explode = [], []
for brand in brands:
    if _max > doc[brand] > _min:
        labels.append(brand)
        sizes.append(doc[brand])

import numpy as np 
import matplotlib.pyplot as plt  
  
   
milage_per_year = 10000



years = list(collection.distinct("year_manufacture"))


values, labels = [], []
for year in years:
    milage = 1000 if ( datetime.datetime.now().year - year ) <= 0 else ( milage_per_year * ( datetime.datetime.now().year - year ) )
    higher = collection.count_documents( { "year_manufacture": year, "milage": {"$gte": milage } } )
    lower = collection.count_documents( { "year_manufacture": year, "milage": {"$lte": milage, "$gte": 1000 } } )
    values.append([ year, higher, lower])


bar_chart(values[-15:-4], labels[-15:-4], [ "Ano", "Quantidade", "Veiculos com menos de 10000km por ano"] )
multiple_bar_chart(values[-15:-4], [ "Ano", "Quantidade", "Veiculos com menos de 10000km por ano"] )