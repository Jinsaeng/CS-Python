##2
##a)
##def shift(lst, k):
##    lst = lst[k:] + lst[0:k]
##    return lst
##def shift_mod(lst,k,direction="left"):
##    if direction == "right" :
##        lst = lst[len(lst)-k:] + lst[0:len(lst)-k] 
##    else:
##        lst = lst[k:] + lst[0:k]
##    return lst
##def main():
##    lst = [1,2,3,4,5,6]
##    k = 2
##    print(lst)
##    print(shift_mod(lst,k,"right"))
##main()
##
##
###3
##
###a)
##def sum_squares(n):
##    total = 0
##    for x in range(n):
##        total += x**2
##    return total
###b)
##    return sum([x**2 for x in range(n)])
###c)
##def sum_odd_square(n):
##    total = 0
##    for x in range(n):
##        if x%2 == 1:
##            total += x**2
##    return total
###d)
##    return sum([x**2 for x in range(n) if x%2==1])
##
###4
##
###a)
##lst_numbers = [10**x for x in range(6)]
##
###b) 1x0, 2x1, 3x2, 4x3, 5x4, 6x5, 7x6, 8x7, 9x8,10x9
##
##lst = [x for x in range(1,11)]
##lst2 = [y for y in range(10)]
##lst_iter = iter(lst)
##lst2_iter = iter(lst2)
##lsnew = []
##for i in range(len(lst)):
##    elem = next(lst_iter)
##    elem *= next(lst2_iter)
##    lsnew.append(elem)

###c)
##lst_alpha = [chr(x) for x in range(ord("a"), ord("z")+1)]

##5
##def fibs(n):
##    curr = 1
##    curr2 = 1
##    yield curr
##    yield curr2
##    for x in range(n-2):
##        num = curr + curr2
##        yield num
##        curr = curr2
##        curr2 = num
        
##        

##6
class Vector:
    def __init__(self,d):
        if isinstance(d,int):
            self.coords = [0] * d
        else:
            self.coords = d
    def  __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self,other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __eq__( self , other ) :
        return self.coords == other.coords
    def __ne__( self , other ) :
        return not (self == other)
    
    def __neg__(self):
        result = self.coords
        for j in range(len(self)):
            result[j] = (-1)* result[j]
        return result
    
    def __mul__(self,other):
        if isinstance(other, int):
            result = self.coords
            for j in range(len(self)):
                result[j] = other* result[j]
            return result
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other[i]
            return result
    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __str__( self ) :
        return "<"+ str(self.coords)[1:-1] + ">"
    def __repr__( self ) :
        return str(self)
    

j = Vector([4,5,6])
i = Vector([1,2,3])
print(i*j)
