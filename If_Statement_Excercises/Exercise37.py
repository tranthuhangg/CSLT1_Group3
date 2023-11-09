NumSides = int(input("Enter the number of sides: "))
if NumSides == 3: 
    shape_name = "triangle"
elif NumSides == 4: 
    shape_name = "quadrilateral"
elif NumSides == 5: 
    shape_name = "pentagon"
elif NumSides == 6: 
    shape_name = "hexagon"
elif NumSides == 7: 
    shape_name = "heptagon"
elif NumSides == 8: 
    shape_name = "octagon"
elif NumSides == 9: 
    shape_name = "nonagon"
elif NumSides == 10: 
    shape_name = "decagon"

print("The shape with",NumSides,"sides is a",shape_name)