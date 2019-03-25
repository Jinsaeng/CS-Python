#4

#a)
lst_numbers = [10**x for x in range(6)]

#b) 1x0, 2x1, 3x2, 4x3, 5x4, 6x5, 7x6, 8x7, 9x8,10x9

lst = [x for x in range(1,11)]
lst2 = [y for y in range(10)]
lst_iter = iter(lst)
lst2_iter = iter(lst2)
lsnew = []
for i in range(len(lst)):
    elem = next(lst_iter)
    elem *= next(lst2_iter)
    lsnew.append(elem)

#c)
lst_alpha = [chr(x) for x in range(ord("a"), ord("z")+1)]
