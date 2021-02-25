import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import math

def getCategories():
    response = requests.get('https://api.mercadolibre.com/sites/MLA/categories')
    return pd.DataFrame(response.json())

def getSubCategories(category):
    response = requests.get('https://api.mercadolibre.com/categories/{}'.format(category))
    return pd.DataFrame(response.json()['children_categories'])

def searchItemsByCategory(category):
    results = []
    offset = 0
    for i in range(0, 20):
        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category={}'.format(category),  
             params={'limit': '50', 'offset': '{}'.format(offset)})
        offset += 50
        results.extend(response.json()['results'])
    return pd.DataFrame(results)

def searchItems(query):
    results = []
    offset = 0
    for i in range(0, 20):
        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?q={}'.format(query),  
             params={'limit': '50', 'offset': '{}'.format(offset)})
        offset += 50
        results.extend(response.json()['results'])
    return pd.DataFrame(results)

def searchItemsDetail(publicactions):
    results = []
    for idx,pub in publicactions.iterrows():
        if(idx % 1000 == 0):
            print("{} of {}".format(idx, publicactions.id.count()))
        response = requests.get('https://api.mercadolibre.com/items/{}'.format(pub.id))
        results.append(response.json())
    return pd.DataFrame(results)
