humanYears = int(input("Human Age: "))
dogYears = 0

if humanYears > 2:
	dogYears = (2 * 10.5) + ((humanYears - 2) * 4)
	print("Dog years: %d" % dogYears)
elif humanYears > 0:
	dogYears = humanYears * 10.5
	print("Dog years: %d" % dogYears)
else:
	print("Error: Age cannot be negative!")

# human_years = int(input("Enter the number of human years: "))

# if human_years < 0:
#     print("Error: The number of human years cannot be negative.")
# elif human_years < 2:
#     dog_years = human_years * 10.5
#     print("The equivalent dog years is",dog_years)
# else:
#     dog_years = 21 + (human_years - 2) * 4
#     print("The equivalent dog years is",dog_years)