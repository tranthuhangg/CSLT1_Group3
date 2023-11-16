prices = []

while True:
    price_str = input("Enter product price: ")
    if price_str == "":
        break
    price = float(price_str)
    prices.append(price)

total_price = sum(prices)

pennies = int(total_price * 100)
remainder = pennies % 5

if remainder < 2.5:
    adjusted_pennies = pennies - remainder
else:
    adjusted_pennies = pennies + (5 - remainder)

cash_payment = adjusted_pennies / 100

print("Total price:", total_price)
print("Cash payment:", cash_payment)