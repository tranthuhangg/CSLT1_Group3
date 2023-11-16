import math

x1 = float(input("Enter the x part of the coordinate:"))
y1 = float(input("Enter the y part of the coordinate:"))

x2 = x1
y2 = y1
perimeter = 0

while True:
    x = input("Enter the x part of the coordinate (blank to quit):")
    if x == "":
        break
    x = float(x)
    y = float(input("Enter the y part of the coordinate:"))

    distance = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)

    perimeter = perimeter + distance

    x2 = x
    y2 = y

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

perimeter = perimeter + distance

print("The perimeter of that polygon is", perimeter)