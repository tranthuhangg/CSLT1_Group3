letter = input("Enter a letter: ")

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The entered letter is a vowel.")
elif letter == 'y':
    print("Sometimes 'y' is a vowel, and sometimes 'y' is a consonant.")
else:
    print("The letter is a consonant.")