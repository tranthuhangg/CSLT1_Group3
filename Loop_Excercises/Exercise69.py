limit = 10
pi = 3
sign = 1

for i in range(1, limit):
	print("%.16f" % pi)
	i *= 2
	pi += sign * (4 / (i * (i + 1) * (i + 2)))
	sign *= -1
