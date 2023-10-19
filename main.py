from petshop_handler import manage_stock


def main():
    print("Main executado")
    print(manage_stock.add_new_product(name="Ração", price=85.5, avaliable_units=5))
   
if __name__ == "__main__": 
    main()
 