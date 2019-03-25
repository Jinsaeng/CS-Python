##def reverse_vowel(str_):
##    ls = list(str_)
##    lsv = []
##    v = ["a","e","i","o","u"]
##    for ele in ls:
##        if ele in v:
##            lsv.append(ele)
##    ls.reverse()
##    j = 0
##    for i in range(len(ls)):
##        if ls[i] in lsv:
##            ls[i] = lsv[j]
##            j+=1
##    ls.reverse()
##    ls = "".join(ls)
##    return ls
##print(reverse_vowel("tandon"))
##import random
##def common(ls1, ls2):
##    ls = []
##    for i in range(len(ls1)):
##        if ls1[i] == ls2[i]:
##            ls.append(ls1[i])
##    return ls
##    ls3 = []
##    for n in ls1:
##        if n not in ls:
##            ls.append(n)
##    for m in ls2:
##        if m in ls:
##            ls3.append(m)
##    return ls3
##ls1 = []
##ls2=[]
##for i in range(1000):
##    ls1.append(random.randint(0,100))
##    ls2.append(random.randint(0,100))
##ls1.sort()
##ls2.sort()
##ls1 = [1,6,14,19]
##ls2 = [2,6,14,23]
##print(common(ls1,ls2))
import math
def square_root(t):
    t = float(t)
    r = t/2.0
    i = 0
    while i < (math.log10(t)+r):
        r = (r+(t/r))/2.0
        i += 1
    return round(r,4)
print(square_root(4))
