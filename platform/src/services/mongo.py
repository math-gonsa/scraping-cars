from pymongo import MongoClient
import os

MONGO_URI = os.environ['MONGO_URI']
MONGO_DATABASE = os.environ['MONGO_DATABASE']

client = MongoClient(MONGO_URI)
database = client[MONGO_DATABASE]
collection = database['cars']

def list_brands():
    return list(collection.distinct("brand"))

def counts(body={}):
    return collection.count_documents(body)


def models_per_brands(brands):
    doc = {}
    
    for brand in brands:
        doc[brand] = collection.distinct("model", {"brand": brand})
    
    return doc

def count_per_models(models):
    doc = {}
    
    for brand in models.keys():
        for model in models[brand]:
                if brand not in doc:
                    doc[brand] = {}
                doc[brand][model] = collection.count_documents( {"brand": brand, "model": model } )    
    
    return doc