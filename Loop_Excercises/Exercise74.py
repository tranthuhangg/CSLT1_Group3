MAX = 15
c = ''

for i in range(MAX + 1):
	for j in range(MAX + 1):
		if i == 0 and j == 0:
			c = " "
		else:
			if i == 0:
				i = 1
			elif j == 0:
				j = 1
			c = str(i * j)
		print("% 5s" % c, end="")
	print()
