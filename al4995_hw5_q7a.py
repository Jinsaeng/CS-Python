num = input("Enter number in the simplified Roman system: ");
m=0
d=0
c=0
l=0
x=0
v=0
one=0
for i in range(0,len(num)):
        if  num[i] == "M":
                m += 1;
        elif num[i] == "D":
                d += 1;
        elif num[i] == "C":
                c += 1
        elif num[i] == "L":
                l += 1
        elif num[i] == "X":
                x += 1
        elif num[i] == "V":
                v += 1
        elif num[i] == "I":
                one += 1
total = (m*1000) + (d*500) + (c*100) + (l*50) + (x*10) + (v*5) + (one*1)
print(m,d,c,v,l,x,v,one)
print(num, "is", total)
