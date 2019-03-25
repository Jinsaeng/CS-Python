#2
#a)
def shift(lst, k):
    lst = lst[k:] + lst[0:k]
    return lst
