def get_brand(x):
    attributes = next(filter(lambda y: y['id'] == 'BRAND', x.attributes), None)
    if attributes is None:
        return None
    else:
        return attributes['value_name']
    
def get_seller_rep(x):
    try:
        return x['seller_reputation']['power_seller_status']
    except:
        return None
    
def get_installments_data(x, field):
    try:
        return x.installments[field]
    except:
        return 0
    
def get_picture_qty(row):
    try:
        return len(row)
    except:
        return 0
    
def get_warrant_time(x):
    try:
        warrant_time = next(filter(lambda y: y['id'] == 'WARRANTY_TIME', x.sale_terms), None)
        if warrant_time is None:
            return None
        else:
            return warrant_time['value_struct']['number']
    except:
        return None
    
def variations_qty(x):
    try:
        return len(x)
    except:
        return 0