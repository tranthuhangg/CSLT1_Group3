prices = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Original Price | Discount Amount | New Price")
print("-------------------------------------------")

for price in prices:
    discount = round(price * 0.6, 2)
    new_price = round(price - discount, 2)
    print("$" + str(price).ljust(14) + "| $" + str(discount).ljust(15) + "| $" + str(new_price))