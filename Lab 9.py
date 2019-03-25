###1
##def consecutive_integers(myint, n):
##    ls = []
##    for i in range(myint, myint+n):
##        ls.append(i)
##    return ls
##
#2
def count(ls, item):
    num = ls.count(item)
    return num
def main():
    ls = [1,1,2,3,4,1]
    item = 1
    print(count(ls,item))
main()
###3
##def main():
##    n = int(input("Enter the power of 2: "));
##    print(powers(n))
##    
##def powers(n):
##    ls = []
##    for i in range(1,n+1):
##        ls.append(2**i)
##    return ls
##
##main()

###4
##
##def find_max_even_index(ls):
##    lsMax = []
##    even = 0
##    for i in range(len(ls)):
##        if (ls[i] % 2 == 0):
##            lsMax.append(ls[i])
##            even += 1
##    if even > 0:
##       high = max(lsMax)
##    return ls.index(high)
##def main():
##    ls = [56, 24, 58, 10, 33, 95]
##    print(find_max_even_index(ls))
##
##main()


###5
##def get_common_element(ls1, ls2):
##    common = []
##    for i in range(len(ls1)):
##        for j in range(i,len(ls2)):
##            if ls1[i] == ls2[j] and ls1[i] not in common:
##                common.append(ls1[i])
##    return common
##def main():
##    ls1 = [2, 2]
##    ls2 = [2, 2]
##    print(get_common_element(ls1,ls2))
##main()

#6
##def square_num(ls):
##    for i in range(len(ls)):
##        ls[i] = (ls[i]**2)
##        end = sum(ls)
##    return end
##def main():
##    ls = [1,2,3,4,5]
##    print(square_num(ls))
##main()

#7
##def remove_below_avg(ls):
##    avg = sum(ls)/ len(ls)
##    above = []
##    for i in range(len(ls)):
##        if ls[i] > avg:
##            above.append(ls[i])
##    return above
##def main():
##    ls = [2, 3, 5, 1, -4, 8, 0, -1]
##    print(remove_below_avg(ls))
##main()

#8
##def circular_shift_list1(ls, k):
##    first = ls[0:len(ls)-k]
##    second = ls[len(ls) - k:]
##    return second+first
##def main():
##    ls = [1, 2, 3, 4, 5, 6, 7, 8]
##    k = 3
##    print(circular_shift_list1(ls,k))
##main()


        
        
