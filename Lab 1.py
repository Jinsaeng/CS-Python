#Lab 1
#Anthony Lam

#1.
#print("Anthony Lam")

#2.

#integer1 = int(input("Please enter the first number: "));
#integer2 = int(input("Please enter the second number: "));
#total = integer1 + integer2;
#multiply = integer1 * integer2;
#subtraction = integer1 - integer2;

#print("Their sum is:", total, ". Their difference is:" ,subtraction, ". Their product is:", multiply);


#3.

#degreesF = int(input("Please enter the appropriate temperature in Fahrenheit: "));
#degreesC = round(((degreesF - 32) * (5/9)), 3);
#print("In Celsius it is:",degreesC ,".", "In Fahrenheit it is:", degreesF);

#4.

#Pounds = int(input("Please enter the number of pounds: "));
#Ounces = Pounds * 16;
#Kilos = Pounds * 0.45;
#print(Pounds, "is equivalent to", Ounces, "ounces and" , Kilos, "kilograms")

#5 and #6 are pencil and paper problems

#7

Length1ft = int(input("Please enter the first length's feet: "));
Length1yd = int(input("Please enter the first length's yards: "));
Length2ft = int(input("Please enter the second length's feet: "));
Length2yd = int(input("Please enter the second length's yards: "));

totalFeet = (Length1ft + Length2ft + (Length1yd * 3) + (Length2yd * 3));
totalYard = int(totalFeet/ 3);
leftoverFeet = totalFeet - (totalYard * 3)

#print(totalFeet)
#print(totalYard)
#print(leftoverFeet)

print( "The sum is:", totalYard, "yards and", leftoverFeet, "feet");
