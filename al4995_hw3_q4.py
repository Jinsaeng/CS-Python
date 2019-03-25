#input 3 float nums
#use the quadratic formula ax^2 + bx + c = 0
#classify the possible options for solution: inf, none, no real, one real, two real
#if there are solutions print them

#b^2 - 4ac determines the # of solutions
# positive = 1 or 2 possible, negative = no real solutions
# if 2a = 0, no real solutions while b and/or c are real numbers
import math 

parA = float(input("Enter value of a: "));
parB = float(input("Enter value of b: "));
parC = float(input("Enter value of c: "));

inside = (parB ** 2) - (4 * parA * parC)
outside = parB * -1

under = 2 * parA

if (parA == 0 and parB == 0 and parC == 0):
    print( "This equation has infinite solutions")
elif (inside < 0):
    print("This equation has no real solutions")
elif (inside == 0):
    print("This equation has one real solution")
    print(outside/under)
elif (inside != 0 and under != 0):
    print("tThis equations has two real solutions: ")
    print("x = ", (outside + math.sqrt(inside)) / under)
    print(("x = ", (outside - math.sqrt(inside)) / under))
else:
    print( "This equation has no solution")
