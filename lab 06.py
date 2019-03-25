##def powers_of_two(num):
##    yield [2**n for n in range(1,num+1)]
##
##for curr in powers_of_two(6):
##    print(curr)

##def total_sum(lst):
##    summ = 0
##    for x in lst:
##        if isinstance(x, int):
##            summ += x
##        else:
##            summ += total_sum(x)
##    return summ            
##print(total_sum([[1, 2], [3, [[4], 5]], 6]))
##

def sort_lst(lst):
    pivot = lst[0]
    left = 1
    right = len(lst) - 1
    while left < right:
        if lst[left] <= pivot:
            left +=1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            right -=1
    print(lst)
    lst[right], lst[0] = lst[0], lst[right]
    return lst

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(sort_lst(lst))


