n = int(input("Enter an integer (2 or greater): "))

if n < 2:
    print("Error: Integer must be 2 or greater.")
else:
    print("The prime factors of", n, "are:")

    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor += 1