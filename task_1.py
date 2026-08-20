def apply_discount(price,discount_percent=5):
    if discount_percent<60:
        discounted_price=price*(1-discount_percent/100)
    else:
        return "Not Applied"
    return discounted_price


print(apply_discount(1000,10))
print(apply_discount(500))
print(apply_discount(500,70))
