#1
##import random 
##num = int(input())
##for i in range (num*2 + 1):
##    if (i < num):
##        out = num-i
##    elif( i >num):
##        out = i-num
##    else:
##        continue
##    for j in range (out):
##        print(random.randint(0,9), end = " ")
##    print()

#2
##def shout (string): #define the name and variable its affecting
##    answer = string.upper()) #define what it does
##    return answer #return it
##
##string = input()
##print(shout(string)) # call back the function and apply it to the variable

#3

def AtoT (string):
    answer = ""
    for i in range (0, len(string),2 ):
        answer += chr(int(string[i:i+2])) #ord --> ascii chr --> char
    return answer

print(AtoT("808984727978"))
