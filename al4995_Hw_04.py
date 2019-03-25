def print_triangle(n):
    res = ""
    if n == 0:
        return ""
    else:
        res =res + print_triangle(n-1) + (n* "*") + "\n"
        return res

def print_opposite_triangles(n):
    res = ""
    if n == 0:
        res = "" + "\n"
        return res
    else:
        res = "\n" + (n)*"*" + print_opposite_triangles(n-1) + ((n)* "*") + "\n"
        return res

def list_min(lst,low,high):
    if low == high:
        return lst[low]
    else:
        if lst[low] < list_min(lst,low+1,high):
            return lst[low]
        else:
            return list_min(lst,low+1,high)


def count_lowercase(s,low,high):
    counter = 0
    if low == high:
        return s[low]
    else:
        res = count_lowercase(s,low+1,high)
        if res.islower():
            counter += 1
        return res,counter


def is_number_of_lowercase_even(s,low,high):
    counter = 0
    if low == high:
        return s[low]
    else:
        res = count_lowercase(s,low+1,high)
        if res.islower():
            counter += 1
    if counter%2 == 0:
        return True
    else:
        return False
def appearances(s,low,high):
    start = 1
    keys = {}
    if low == high:
        return s[low]
    else:
        appearances(s,low+1,high)
        if s[low] not in keys:
            keys = {s[low] : start}
        else:
            keys[s[low]: start+1]
        return keys
        
        
def split_by_sign(lst,low,high):
    if low == high:
        return low
    else:
        if lst[low] > lst[high]:
            res = res+ split_by_sign(lst, low+1, high)
        else:
            res = split_by_sign(lst,low+1,high) + res
        return res
    
def flat_list(nested_list, low, high):
    newls = []
    if low==high:
        return nested_lst[low]
    else:
        for x in nested_list:
            if isinstance(x, int):
                newls.append(x)
                return newls
            elif isinstance(x, list):
                flat_list(nested_list,low+1,high)
    return newls

def permutations(lst, low, high):
    newls= []
    val = []
    if low == high:
        return lst[low]
    else:
        val = [permutation(lst,low+1,high)]
        newls.append(val)
        return newls
