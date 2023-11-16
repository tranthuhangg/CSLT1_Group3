total_cost = 0
num_guests = 0

while True:
    age_input = input("Enter the age of a guest (blank to finish): ")
    if age_input == "":
        break

    age = int(age_input)
    
    if age <= 2:
        cost = 0
    elif 3 <= age <= 12:
        cost = 14
    elif age >= 65:
        cost = 18
    else:
        cost = 23

    total_cost += cost
    num_guests += 1

if num_guests > 0:
    print("The admission cost for the group is $",round(total_cost,2))
else:
    print("No guests in the group.")