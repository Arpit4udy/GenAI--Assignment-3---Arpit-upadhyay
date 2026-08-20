prices=[100,250,400,1200,500]

#applying GST to each price
final_prices=map(lambda price:price+price*0.18,prices) 
print(f"Original Prices : {prices}")
print(f"Prices after GST:{list(final_prices)}")
