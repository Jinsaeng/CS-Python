import math
def factors (num):
    lst = []
    for i in range(1, math.ceil(math.sqrt(num))):
        if num% i == 0:
            lst.append(i)
            yield i
    lst.reverse()
    for ele in lst:
        i = int(num/ele)
        yield i
