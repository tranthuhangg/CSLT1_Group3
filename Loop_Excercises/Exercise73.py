string = input("Enter String: ").replace(" ", '').lower()

l = len(string)
isPalindrome = True
for i in range((l // 2)):
	if string[i] != string[-i - 1]:
		isPalindrome = False
		break

print("String is ", end="")
if not isPalindrome: print("not ", end="")
print("a Palindrome")

