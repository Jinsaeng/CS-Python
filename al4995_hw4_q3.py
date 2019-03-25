columns = 5;
rows = 10;
for i in range(1,columns + 1):
    print (" ")
    for j in range(1, rows + 1):
        num = j ** i
        print(num,sep = "", end = "\t" )
