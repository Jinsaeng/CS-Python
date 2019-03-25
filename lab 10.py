class Polynomial:
    def __init(self, lst):
        self.coeff = lst
        self.poly = ""
    def construct(self,lst):
        self.poly = ""
        for i in range(1,len(lst)+1):
            if lst[i-1] == 0:
                self.poly += ""
            else:
                if i == len(lst):
                    self.poly += str(lst[len(lst)-i])
                else:
                    self.poly =  self.poly + str(lst[len(lst)-i]) + "x" + "^" + str(len(lst)-i) + " + "
    def __repr__(self):
        return self.poly
    def eval(self,val):
        for i in range(len(lst)):
             if lst[len(lst)-i-1] == val:
                 return lst[i]

            
lst = [3,7,0,-9,2]
poly = Polynomial()
poly.construct(lst)
poly = poly.eval(1)
print(poly)



def func(lst):
    length = len(lst)
    return [lst[i] for i in range(length) if i%2 == 0 and lst[i] %2 == 0]
print(func([2,3,5,6,8,8,8,8,8,8,8,8,8,8,8]))
