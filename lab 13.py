def most_frequent(lst):
    list = the numbers already seen
    for loop running through list:
        while loop: if the new number is not in list
            if next number == orignial number
            counter + = 1

        counter compare to old counter
        highest count = bigger counter

def most_frequent(lst):
    nums_seen = {}
    for i in lst:
        if i in nums_seen:
            nums_seen[i] += 1
        else:
            nums_seen[i] = 1
    max_num = 0
    max_count = 0
    for i in nums_seen:
        if nums_seen[i] > max_count:
            max_count = nums_seen[i]
            max_num = i
    return max_num
#worst case n^2, avg case n



class OpenAddressingHashMap:
    class Item:
        def __init(self,key,value=None):
            self.key = ket
            self.value = value
    def __init__ (self, N, n = 0):
        self.N = N
        self.n = n
        self.table = [None] * self.N
    def __len__(self):
        return self.n
    def is_empty(self):
        return (if self.N != 0)
    def __getitem__(self, k):
        item = k % self.N
        curr = self.table[item]
        if curr is None:
            raise KeyError("Key does not exist")
        return curr[k]
    def __setitem__(self,k,v):
        item = k % self.N
        if self.table[item] is None:
            self
        pass
    def __delitem__(self,k,v):
        #deal with None
        #deal with empty bucket afterwards
        pass
    def __iter__(self):
        pass
    def rehash(self,new_size):
        self.N = new_size
        for item in self.table:
            curr = self.table[item]
            item = curr % self.N
        
