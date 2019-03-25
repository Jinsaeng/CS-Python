loop = int(input("Please enter the length of the sequence: "));
entered = 1
for i in range(1, loop+1):
    entered *=  int(input());

mean = (entered ** (1/loop))
print(mean)

