side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

if side1 == side2 == side3:
    triangle_type = "Equilateral triangle"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles triangle"
else:
    triangle_type = "Scalene triangle"

print("The triangle is:", triangle_type)