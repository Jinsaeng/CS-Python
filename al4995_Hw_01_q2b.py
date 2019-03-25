#b)
def shift_mod(lst,k,direction="left"):
    if direction == "right" :
        lst = lst[len(lst)-k:] + lst[0:len(lst)-k] 
    else:
        lst = lst[k:] + lst[0:k]
    return lst
