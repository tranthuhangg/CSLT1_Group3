binary = input("Enter a binary number: ")
decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)
print("The equivalent decimal number is:", decimal)