def process_prices(price):
    discounted_prices=list(map(lambda x:x*(1-0.1),price))  # 10 percent discount
    filtered_prices=list(filter(lambda x:x>300,price))
    print(discounted_prices)
    print(filtered_prices)

process_prices([100,500,900,50,750])

