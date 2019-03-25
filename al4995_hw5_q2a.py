char = input("Enter a character: ")
num = ord(char)
if  char.isdigit():
    title = "digit"
elif char == "!" or char == "@" or char == "$" or char == "&":
    title = "non-alphanumeric character"
elif char.upper() == char:
    title = "upper case letter"
elif char.lower() == char:
    title = "lower case letter"
print(char, "is a", title)
