line= input("Please enter a line of text: ")
remove = input("Character to remove: ")
newline = "";
for i in range(0,len(line)):
    if line[i] == remove:
          newline += " "
    else:
        newline += line[i]
print(newline)
