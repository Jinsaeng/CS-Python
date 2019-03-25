char = input("Enter a character: ")
num = ord(char)

if num > 96 and num <123 :
    title = "lower case letter"
elif num >64 and num < 91:
    title = "upper case letter"
elif num > 47 and num < 58:
    title = "digit"
else:
    title = "non- alphanumeric character"
print(char, "is a", title)
