

def find_lst_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_lst_max(lst[1:]))
def find_lst_max(lst):
    if len(lst)==1:
        return lst[0]
    elif lst[0] < lst[1]:
        return find_lst_max(lst[1:])
    elif lst[-1] < lst[-2]:
    return find_lst_max(lst[:-1])
print(find_lst_max([0,1,2,100,3,5,8,101, 200,10]))

def product_evens(lst):
    count = 0
    n = len(lst)+count
    if n == 1 and lst[0] % 2 == 0 :
        return lst[0]
    else:
        if (lst[0] % 2 == 0) and lst[0] <= n:
            count += 1
            return lst[0] *product_evens(lst[1:])
        else:
            return product_evens(lst[1:])
print(product_evens([1,2,3,4,5,100,12,2]))


def is_palindrome(string, low, high):
    if low >= high:
        return True
    else:
        if string[low] == string[high]:
            return is_palindrome(string, low+1, high-1)
        else:
            return False
