prices_list=[]
def add_prices(prices_list,price):
    prices_list.append(price)
    print(f"Prices List:{prices_list}")

def get_average_price(prices_list):
    total=0
    if not prices_list:
        print("Not Valid")
    else:    
      for i in prices_list:
         total+=i
      print(f"Average Price: {total/len(prices_list)}")    
    


def get_max_price(prices_list):
    if not prices_list:
        print("Not Valid")
    else:
     maximum=prices_list[0]
     for i in prices_list:
         if maximum<i:
            maximum=i
     print(f"Maximum price: {maximum}")   


while True:
    print("\n--- Price Menu ---")
    print("1. Add Price")
    print("2. Show Average Price")
    print("3. Show Highest Price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_prices(prices_list, price)

    elif choice == "2":
        get_average_price(prices_list)

    elif choice == "3":
        get_max_price(prices_list)

    elif choice == "q":
        print("Quitting...")
        break

    else:
        print("Invalid Choice")
        








    