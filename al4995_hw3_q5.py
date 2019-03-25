import math
print("Please enter lengths of a triangle's sides");
side1 = float(input("Length of first side: "));
side2 = float(input("Length of second side: "));
side3 = float(input("Length of third side: "));
print("Possible triangles are: equilateral, right angle isosceles, and an isosceles triangle.");
if(abs(side1 - side2) < 0.00001):
    side1 = side2
elif(abs(side1 - side3) < 0.00001):
    side1 = side3
elif(abs(side2 - side3) < 0.00001):
    side2 = side3

if (side1 == side2 and side2 == side3):
    print(side1, side2, side3, "form an equilateral triangle.")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    side1squ = side1**2
    side2squ = side2**2
    side3squ = side3**2
    if abs(side1squ + side2squ - side3squ)  < 0.00001 or abs(side2squ + side3squ - side1squ) < 0.00001 or abs(side1squ + side3squ - side2squ) < 0.00001:
        print( side1, side2, side3, "form a right angle isosceles triangle.")
    else:
        print(side1, side2, side3, "form an isosceles triangle")
else:
    print(side1, side2, side3, "do not form an aforementioned triangle.")
