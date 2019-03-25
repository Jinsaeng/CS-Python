class polynomial:
    def __init__(self, list_of_coeff = None):
        self.ls = list_of_coeff
    def construct(self, ls):
        if self.ls == None:
            return "p(x) = 0"
        else:
            p = len(self.ls)
            self.ls = [ (ls[p]) for x in range(p)]
    def eval (self, val):
        return self.ls[val]
    def add (ls, ls2):
        newls = [ls[x] + ls2[x] for x in range(len(ls))]
        string = ""
        for i in range(len(newls)-1, -1, -1):
            if i > 0:
                if newls[i]  > 0:
                    string += (" + " + str(newls[i]) + "x^" + str(i) + " ")
                elif newls[i] < 0:
                    string += (str(newls[i]) + "x^" + str(i) + " ")
                else:
                    string += ""
            elif i == 0: 
                if newls[i] > 0:
                    string += (" + " + str(newls[i]))
        return str(string)
##    def __mult__(self,rhs):
##        res = [0] * (len(self.coeff) + len(rhs.coeff) - 1)
##        for i in range(len(self.coeff)):
##            for j in range(len(rhs.coeff)):
##                res[i+j] += self.coeff[i] * self.rhs[j]
##        return Poly(res)
    def __repr__(self):
        string = ""
        for i in range(len(self.ls)-1, -1, -1):
            if i > 0:
                if self.ls[i]  > 0:
                    string += (" + " + str(self.ls[i]) + "x^" + str(i) + " ")
                elif self.ls[i] < 0:
                    string += (str(self.ls[i]) + "x^" + str(i) + " ")
                else:
                    string += ""
            elif i == 0: 
                if self.ls[i] > 0:
                    string += (" + " + str(self.ls[i]))
        return str(string)
        
def main():
    ls = ([3,7,1,-9,2])
    ls2 = ([0,9,0,0,0,0,0,0,0,3])
    print(polynomial(ls))
    print(polynomial(ls2))
main()


###2
##ls = [2,3,5,6,8,8,6,10,4,4]
##ls = [ls[i] for i in range(len(ls)) if (i%2 == 0) and (ls[i] % 2 == 0)]
##newls = []
##dup = input("Duplicates? (Y/N):")
##if dup == "N":
##    for i in (ls):
##        if i not in newls:
##            newls.append(i)
##elif dup == "Y":
##    newls = ls
##else:
##    print("Error in selection")
##print(newls)
