import turtle
import math

side1 = int(input("Please input a value for the first side:"));
side2 =  int(input("Please input a value for the second side:"));
angle = int(input("Please input a value for the angle between the two sides:"));

turtle.forward(side1)
turtle.left(180-angle)
turtle.forward(side2)

#if( angle > 90 and angle < 180):
#    angle -= 90
#    sign = -1
#else:
#    sign = 1
#if the angle is greater than 90, convert so that its in the first quadrant and then
#work with the angle in radian and take into account of the negative
    
angle = angle* math.pi / 180
#convert the angle into radians and then plug the value into the math function
#since the math function outputs a radian from the cosine

print (angle)
#angle in radian

side1sqr = math.pow(side1,2)
side2sqr = math.pow(side2,2)

coss1s2 = (math.cos(angle)) * 2 * side1 * side2
#but it doesn't output a radian because i plugged into my calculator and got the answer in degrees?
#worked in the calculator

print(coss1s2)
side3 = math.sqrt(side1sqr + side2sqr -coss1s2);
print(side3)

#got the "correct length for the final side so that I can tell the turle to move that many space
#combined with the correct angle, should connect to the start of the first side

#law of sine = sin(a)/A = sin(c)/C
#want to isolate angle a
# sin^-1(sin(c)* A) /C) = a

AngleB = math.asin((math.sin(angle) * side1) / side3)
print(AngleB)
turtle.left(math.degrees(math.pi-AngleB))
turtle.forward(side3)
#best way to do it was to do everything in radians and convert it to degrees only when turning in turtle
