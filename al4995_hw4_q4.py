num = int(input("Enter number: "));
###code for left justified 

for i in range(num+1):
    print("  " * ((num+1) - (i+1)), end = "")
    for j in range(i):
        print(j+1, end = "")
    print()

