x = int(input("Number: "))
g = (x / 2)

while abs((g * g) - x) > 1e-12 :
	g = (g + (x / g)) / 2
	print("%.4f" % g)

print("Approx. Val: %.6f" % g)
