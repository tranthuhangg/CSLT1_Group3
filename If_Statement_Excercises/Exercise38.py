month = input("Month: ")

if month == "February":
    year = int(input("Year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 29
    else:
        days = 28
elif month in ["April", "June", "September", "November"]:
    days = 30
else:
    days = 31

print("The month of",month,"has",days,"days.")