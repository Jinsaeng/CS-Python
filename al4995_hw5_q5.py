password = input("Enter your password: ");
digit = 0
upper = False
lower = False
special = False
number = False
for i in range(len(password)):
    if ord(password[i]) < 123 and ord(password[i]) > 96:
        lower = True;
    elif ord(password[i]) < 91 and ord(password[i]) > 64:
        upper = True
    elif ord(password[i]) < 58 and ord(password[i]) >48:
        digit +=1
    elif ord(password[i]) == 33 or ord(password[i]) == 35 or ord(password[i]) == 36 or ord(password[i]) == 38:
        special = True
    if digit >= 2:
        number = True
if lower and upper and number and special:
    print("Password is valid")
else:
    print("Password is invalid")



