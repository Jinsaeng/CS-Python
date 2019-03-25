num = (input("Enter a decimal number: "))
result = int(num)
newstr = "";
while result != 0:
    for i in range(0,len(num)):
        if result // 1000 >= 1:
            newstr += "M"
            result -= 1000
        elif result // 500 >= 1:
            newstr += "D" 
            result -= 500
        elif result // 100 >= 1:
            newstr += "C" 
            result -= 100
        elif result // 50 >= 1:
            newstr += "L" 
            result -= 50
        elif result // 10 >= 1:
            newstr += "X"
            result -= 10
        elif result // 5 >= 1:
            newstr += "V" 
            result -= 5
        elif result // 1 >= 1:
            newstr += "I"
            result -= 1
print(newstr);
