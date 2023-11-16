print("Temperature Conversion Table")
print("---------------------------")
print("Celsius".ljust(8) + "Fahrenheit")

for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(str(celsius).ljust(8) + str(fahrenheit))