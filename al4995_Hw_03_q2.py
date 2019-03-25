import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)
#2
#a)
    def insert(self, index, val):
        if index < self.n:
            newls = []
            first = self.data[0:index-1]
           end = self.data[index:]
            newls = first + val + end
            return newls
        else:
            raise IndexError("Invalid Index")
#b)
    def pop(self):
        if self.n > 0:
            return self.data[0:self.n-1]
        else:
            raise IndexError("Invalid index")
        

    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)) and ((-1 * ind) < (-1 * len(self.n))):
            raise IndexError('invalid index')
        elif ind < 0:
            return self.data[self.n + ind]
        else:
            return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)) and ((-1 * ind) < (-1 * len(self.n))):
            raise IndexError('invalid index')
        elif ind < 0:
            self.data[self.n + ind] = val
        else:
            self.data[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]
            
    def __repr__ (self):
        return "[".join(str(i) for i in self) + "]"

