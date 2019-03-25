combo = input("Enter a string of only lowercase letters: ")
top = 0
previous = 0
for i in range(0,len(combo)):
    if ord(combo[i]) > previous:
        top += 1
        previous = ord(combo[i])
if top == len(combo):
    order = "increasing"
else:
    order = "not increasing"
print(combo, "is", order)
