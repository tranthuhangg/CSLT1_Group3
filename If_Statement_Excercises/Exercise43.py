denomination = int(input("Enter the denomination of a banknote: $"))

if denomination == 1:
    print("George Washington appears on the $1 banknote.")
elif denomination == 2:
    print("Thomas Jefferson appears on the $2 banknote.")
elif denomination == 5:
    print("Abraham Lincoln appears on the $5 banknote.")
elif denomination == 10:
    print("Alexander Hamilton appears on the $10 banknote.")
elif denomination == 20:
    print("Andrew Jackson appears on the $20 banknote.")
elif denomination == 50:
    print("Ulysses S. Grant appears on the $50 banknote.")
elif denomination == 100:
    print("Benjamin Franklin appears on the $100 banknote.")
else:
    print("No such note exists.")