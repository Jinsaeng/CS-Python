def split_by_sign(lst,low,high):
    if low == high:
        return low
    else:
        if lst[low] > lst[high]:
            res = res+ split_by_sign(lst, low+1, high)
        else:
            res = split_by_sign(lst,low+1,high) + res
        return res
