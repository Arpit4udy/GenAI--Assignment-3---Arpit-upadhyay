prices=[100,250,400,1200,50,2000,850]
list_1=list(filter(lambda price:price>500,prices))
list_2=list(filter(lambda price:price<=500,prices))
print(list_1)
print(list_2)
