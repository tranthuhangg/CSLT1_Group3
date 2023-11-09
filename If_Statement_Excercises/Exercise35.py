HumanYear = int(input("Enter Human years: "))

if HumanYear < 0:
    print("Error: Human years cannot be negative.")
else:
    if HumanYear < 2:
        DogYear = HumanYear * 10.5
    else:
        DogYear = 21 + (HumanYear - 2) * 4
    
    print("The equivalent dog years is", DogYear)
    
