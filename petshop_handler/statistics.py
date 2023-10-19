def get_price_average(products: list[dict]): 

    total_value = 0
    for product in products:
        total_value += product["price"]
    average = total_value / len(products)
    return f"Média: {average}"