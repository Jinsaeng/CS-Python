#3

#a)
def sum_squares(n):
    total = 0
    for x in range(n):
        total += x**2
    return total
#b)
    return sum([x**2 for x in range(n)])
#c)
def sum_odd_square(n):
    total = 0
    for x in range(n):
        if x%2 == 1:
            total += x**2
    return total
#d)
    return sum([x**2 for x in range(n) if x%2==1])

