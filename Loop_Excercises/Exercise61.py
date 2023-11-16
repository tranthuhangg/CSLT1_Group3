value=float(input("value="))
count=0
total=0
if value == 0:
    print("Error: No values to calculate the average.")
else:
    while value!=0:
        count=count+1
        total=total+value
        value=float(input("value="))
        
    average=total/count
    print("Average =",average)

