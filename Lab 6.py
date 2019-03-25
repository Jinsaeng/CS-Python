###1
##userString = input("Please enter a string: ");
##for i in range(0:len(userString)):
##    if (not(userString.isupper[i])):

#2
##a1 = input("Enter string a: ")
##b1 = input("Enter string a: ")
##
##if len(a1) < len(b1):
##    print(a1, b1, a1, sep = "")
##else:
##    print(b1,a1,b1, sep = "")

###3
##s1 = input("Please enter a string s: ")
##k1 = int(input("Please enter a number k: "));
##sub1 = ""
##reverse = True
##for i in range(0, len(s1), k1):
##    if (i+k1 > len(s1)):
##        sub1 += s1[i:]
##    else:
##        sub = s1[i:(k1+i)]
##        if (reverse):
##            sub1 += sub[::-1]
##            reverse = False
##        else:
##            sub1 += sub
##            reverse = True
##print(sub1)
##

#4
##s1= input("Please enter string s: ")
##s = " " + s1
##num = (s.find(" "))
##for i in range (0,len(s)):
##        sub = s[i:s.find(" "): -1]
##        if (s.find(" ") != -1):
##            start = s.find(" ");
##            end = s.find(" "); + 1
##            sub += s[start: end: -1]
##        else:
##            sub += s[i:]
##print(sub)
##print("Palindrome =", s,"" ,sub)
###reverse words AND order of words 

#5
s = input("String: ");
length = len(s)
sub = ""
for i in range( len(s)+1):
    if (s[i] != s[i+1]):
        sub += s[i]
    else:
        sub = s[i]
print(sub)
        













