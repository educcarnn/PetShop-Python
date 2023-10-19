from petshop_handler import manage_stock
from petshop_handler import statistics
from stock import products

def main():
    print("Main executado")
    print(manage_stock.add_new_product(name="Ração", price=85.5, avaliable_units=5))
    print(statistics.get_price_average(products))


if __name__ == "__main__": 
    main()
 