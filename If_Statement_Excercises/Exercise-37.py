numSides = int(input("Enter the number of sides: "))
if numSides == 3: 
    shape_name = "triangle"
elif numSides == 4: 
    shape_name = "quadrilateral"
elif numSides == 5: 
    shape_name = "pentagon"
elif numSides == 6: 
    shape_name = "hexagon"
elif numSides == 7: 
    shape_name = "heptagon"
elif numSides == 8: 
    shape_name = "octagon"
elif numSides == 9: 
    shape_name = "nonagon"
elif numSides == 10: 
    shape_name = "decagon"

print("The shape with",numSides,"sides is a",shape_name)