gst = lambda price:(price+0.18*price)
print(gst(100))

#optional-- final price after discount
final_price=lambda price,discount:gst(price)-gst(price)*discount/100
print(final_price(100,6))
