#Lab 3
#Skip 1 & 2
import math

#3
#leg1=float(input("Please enter the first leg:"));
#leg2=float(input("Please enter the second leg:"));
#hypot =float(input("Please enter the hypotenuse:"));

#hypothesis = (math.hypot(leg1,leg2);

#if(hypothesis == hypot):
#    print(leg1, ",", leg2, ", and", hypot, "form a right triangle");
#else:
#    print("it does not");
            

#4
#print("Solve the equation ax + b = 0 by inputing the integers");
#integerA= int(input("Please enter the integer A: "));
#integerB = int(input("Please enter the integer B: "));

#if (integerA != 0 ):
#    solution = -(1 * integerB) / integerA;
#    print("The single solution to", integerA, "x +", integerB, " = 0, is x =", solution);
#elif(integerA == 0 and integerB != 0):
#    print("No solution");
#else:
#      print("There are infinite solutions");


#5
#integer = int(input("Please enter an integer between 1 and 12 inclusive: "));

#if (integer == 1 or integer == 3 or integer == 5 or integer == 7 or integer == 8 or integer == 10 or integer == 12):
#    days = 31;
#    if (integer == 1):
#        print("The month is January, and the number of days in January is",days, ".");
#    elif(integer == 3):
#        print("The month is March, and the number of days in March is", days,".");
#    elif(integer == 5):
#        print("The month is May, and the number of days in May is", days,".");        
#    elif(integer == 7):
#        print("The month is July, and the number of days in July is", days,".");
#    elif(integer == 8):
#        print("The month is August, and the number of days in August is", days,".");
#    elif(integer == 10):
#        print("The month is October, and the number of days in October is", days,".");
#    elif(integer == 12):
#        print("The month is December, and the number of days in December is", days,".");
#elif (integer == 2):
#    print("The month is February, and the number of days in February is 28");
#else:
#    days = 30;
#    if(integer == 4):
#        print("The month is April, and the number of days in April is ", days,".");
#    elif(integer == 6):
#        print("The month is June, and the number of days in June is ", days,".");
#    elif(integer == 9):
#        print("The month is September, and the number of days in September is", days,".");
#    elif(integer == 11):
#        print("The month is November, and the number of days in November is", days,".");

#6

#sides = int(input("Please enter the number of sides: "));
#if (sides == 3):
#    print("The shape is a triangle.");
#elif(sides == 5):
#    print("The shape is a pentagon.");
#else:
#    Equalside = input("Are the sides equal? (Y/N): ");
#    Angle = input("Are the angles 90 degrees? (Y/N): ");
#    if(Equalside == "Y" and Angle == "Y"):
#        print("The shape is a square.");
#    elif(Equalside != "Y" and Angle == "Y"):
#        print("The shape is a rectangle.");
#    elif(Equalside != "Y" and Angle != "Y"):
#        print("The shape is a quadrilateral.");
#    else
#        print("Invalid shape.");

#7
timeS = int(input("Please enter time in 24 hr format: "));

hours = (timeS // 100);
minutes = (timeS % 100);
if (minutes < 10):
    minutes = "0" + str(minutes)

if (hours > 12):
    hours2 = (hours - 12);
    tod = "pm"
else:
    hours2 = hours
    tod = "am"

print(hours,":",minutes,"in 12 hr format is:", hours2,":",minutes, tod);
    



