1
num = int(input("Please enter a number: "));

for i in range(1,num+1):
    print("")
    for j in range(1,i+1):
        print(j, end="");
            

#2
#num = int(input("Please enter a number: "));

#for i in range(1,num+1):
#    print((num-i)* "." + str(i)*i)

#3
#num = int(input("First number: "))
#num2 = int(input("Second number: "))
##length = len(num1)
##count = 0
##print(length)
##for i in range(length):
##   if (num1 - num2)
##      count += 1
##print("hamming is", count)


#count = 0;
#while(num > 0):

#    if ((num%10) != (num2 %10)):
#        count += 1
#    num //= 10;
#    num2 //= 10;
#print(count)

#4
#import turtle

#sides = int(input("sides? :"))
#angle = ((sides - 2) * 180)/sides

#for i in range(1, sides + 1):
#    turtle.forward(100)
#    turtle.left((180- angle))
#    turtle.forward(90)

#5
#import random
#rand = random.randrange(1,101)
#guess = int(input("Guess the number between 1 and 100: "));
#while (guess != rand):
#    if (rand < guess):
#        print("Lower");
#        guess = int(input("Guess again: "));
#    elif( rand > guess):
#        print("Higher");
#        guess = int(input("Guess again: "));
#print("You got it.");




