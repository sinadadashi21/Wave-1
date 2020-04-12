import math
r = float(input("Enter the radius of the cylinder in metres: "))
h = float(input("Enter the height of the cylinder in metres: "))
area = math.pi * r**2
volume = area * h
volume = round(volume, 1)
print("The volume of the cylinder is: " + str(volume) + " metres cubed")

