from stock import products

def add_new_product(**kwargs: dict):
    try:
        received_product = {
            "name": kwargs["name"],
            "price": kwargs["price"],
            "avaliable_units": kwargs["avaliable_units"]
        }
    except KeyError:
        return "Estão faltando chaves obrigatórias no dicionário."
    
    if not products:  
        products.append(received_product)
        return received_product
    
    for current_product in products:
        if current_product["name"] == received_product["name"]: 
            current_product["avaliable_units"] += received_product["avaliable_units"]
            return f"Produto com nome {current_product['name']} foi reabastecido"