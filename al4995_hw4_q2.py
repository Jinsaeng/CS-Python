num = int(input("Please enter a positive integer: "));
seq = 2* num
for i in range(0, seq ,  2):
    print( " " * (i*2) + (seq - (i+1)) * " *  ")
for i in range(seq, -1 , -2):
    print( " " * (i*2) + (seq - (i+1)) * " *  ")
