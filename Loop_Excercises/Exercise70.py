az = "abcdefghijklmnopqrstuvwxyz" 
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = input("Plaintext: ")
shift = int(input("Shift Amount: "))
ciphertext = []

for c in plaintext:
	if c.isalpha():
		if c.islower():
			ciphertext.append(az[(az.find(c) + shift) % 26])
		elif c.isupper():
			ciphertext.append(AZ[(AZ.find(c) + shift) % 26])
	else:
		ciphertext.append(c)

print(''.join(ciphertext))