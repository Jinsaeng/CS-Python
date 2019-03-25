def split_parity(lst):
    n = len(lst)
    count = 0
    count2 = 0
    for ele in range(n):
        if lst[ele]%2 == 0:
            count += 1
            starter = ele
        elif lst[ele]%2 == 1:
            count2 += 1
            starter2 = ele
            while (count >0 and count2 > 0):
                lst[starter2], lst[starter] = lst[starter],lst[starter2]
                count -= 1
                count2 -= 1
    return lst
