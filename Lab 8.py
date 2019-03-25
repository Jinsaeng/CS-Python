#1
##def consecutive_letter(ch, n):
##    count = 1
##    string = ch;
##    while count < n:
##        new = ord(ch) + 1
##        if new > 122:
##            new -= 26
##        string += chr(new)
##        ch = chr(new)
##        count += 1
##    return string

#2
##def string_fit(a,b)
##    for i in range(len(a)):
##        if b.find(a[i]) != -1:
##            b.replace(b[i], "")
##            string = True;
##        else:
##            string = False;
##    return string

#3
##def encode_binary(string):
##    count = 0
##    pos = 0
##    rep = ""
##    string = ""
##    for i in range(len(binary)):
##        start = binary[i]
##        if start == binary[pos]:
##            count += 1
##        else:
##            pos = i
##            rep += str(count)
##            rep +=  " " + binary[i-1] + "'s \n"
##            count = 1
##    rep += str(count)
##    rep +=  " " + binary[i-1] + "''s \n"
##
##    return rep

####binary = input("Binary: ");
####count = 0
####pos = 0
####rep = ""
####string = ""
####for i in range(len(binary)):
####    start = binary[i]
####    if start == binary[pos]:
####        count += 1
####    else:
####        pos = i
####        rep += str(count)
####        rep +=  " " + binary[i-1] + "'s \n"
####        count = 1
####rep += str(count)
####rep +=  " " + binary[i-1] + "''s \n"
####print(rep)



#4
##def flipping(string):
##    new = 0
##    for i in range(len(string)):
##        if string[i] == "0":
##            new += (2**(len(num)-i-1))
##    return new

####num =input("string:")
####new = 0
####for i in range(len(num)):
####    if num[i] == "0":
####        new += (2**(len(num)-i - 1))
####print(new)
