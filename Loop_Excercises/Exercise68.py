import re

while True:
	s = input("Enter String: ")
	if s == "":
		break
	elif len(s) != 8 or not re.match(r'^[01]+$', s):
		print("ERR!")
		break

	c = s.count('1')
	p = c % 2
	print("Parity Bit: %d" % p)
