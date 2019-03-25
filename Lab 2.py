#   101101_2  --> _10
#   [0][0]32[0]8[4]0[1]
#   =45
# 
#   FD41_16 --> _10
#   [1111][1101][0100[[0001]
#   [][][][][][][][][][][4168]2084[1042]0[256]0[64]0[0]0[0]0[1]
#
#
#
#
#skip 1,3
import math
import turtle

#1
#radius = int(input("Enter an integer radius:"));
#circumference = round( 2 * math.pi * radius,4);
#area = round(math.pi * radius**2,4)

#print("The circumference of the circle is:",circumference,"and the area of the circle is:",area);
 
#2
#turtle.forward(100)
#turtle.left(72)
#turtle.forward(100)
#turtle.left(72)
#turtle.forward(100)
#turtle.left(72)
#turtle.forward(100)
#turtle.left(72)
#turtle.forward(100)

#3
#days =int(input("Enter the number of days:"));

#weeks = days//7
#newDays = days%7

#print(days,"days is equal to",weeks,"week(s) and",newDays,"days.");

4
num = int(input("Enter a number:"));
L = num//50
num = num%50
X = num//10
num = num%10
V = num//5
num = num%5
I = num

print("L"*L + "X"*X + "V"*V + "I"*I);

#5
##birthday =int( input("Enter a date of birth in standard format (yyyymmdd):"));
##today = int(input("Enter today's date in standard format:"));
##
##
##year = birthday // 10000
##birthday = birthday % 10000
##month = birthday // 100
##birthday= birthday % 100
##day = birthday
##
##year2 = today // 10000
##today = today % 10000
##month2 = today // 100
##today = today % 100
##day2 = today
##
###print(month, "/",day,"/",year);
###print(month2,"/",day2,"/",year2);
##
##print(day, day2)
##print(year,year2)
##print(month,month2)
##ageYears = (year2-year) 
##ageMonths = (month2- month)
##ageDays = (day2- day)
##daysAlive = (ageYears*365) + (ageMonths*30) + ageDays
##print(daysAlive)
##yearsAlive = daysAlive // 365
##print(daysAlive)
##daysAlive = daysAlive % 365
##print(daysAlive)
##monthsAlive = daysAlive // 30
##print(daysAlive)
##daysAlive = daysAlive % 30
##
##
##print("You have been alive for",yearsAlive,"years,",monthsAlive,"months, and",daysAlive,"days.");
##
##if (month < month2) :
##    month = month + 12
##else:
##    month = month + 0
##monthsleft = abs(month2 -month )-1;
##
##
##if (day > day2):
##    day = day + 30
##    monthsleft = monthsleft + 1
##else:
##    day = day + 0
##    
##daysleft = abs(day2-day);
##daysleft = abs(daysleft -30)
##
##if daysleft > 30:
##    daysleft = daysleft -30
##    monthsleft = monthsleft + 1
##else:
##    daysleft = daysleft + 0
##    
##print(monthsleft, "months and,",daysleft,"days left until ur next bday.");
##
##
##daysleft2 =daysleft + (monthsleft * 30)
##print(daysleft2,"days left til ur next bday");
##
##
##
##
##
