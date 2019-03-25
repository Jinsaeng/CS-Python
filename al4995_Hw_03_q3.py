def find_duplicate(lst):
    dup = []
    lst.sort()
    length = len(lst)
    lst.append(0)
    count = 0
    for i in range(length):
        a = lst[i]
        if lst[i+1] == a and count < 1:
            count += 1
            dup.append(lst[i])
        else:
            count = 0
    return dup
print(find_duplicate([1,1,2,2,2,3,4,5,6,7,7,7,9]))
