
import math
class Empty(Exception):
    pass
    
class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
        
class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    
def permutations(lst):
    length = len(lst)
    arrayS = ArrayStack()
    arrayQ = ArrayQueue()
    numofperm = math.factorial(length)
    rotation = 0
    newlst = lst
    while rotation < numofperm:
        for i in newlst:
            arrayS.push(i)
        for x in range(length):
            item = arrayS.pop()
            newlst.append(item)
        arrayQ.enqueue(newlst)
        rotation += 1
        newlst = newlst[length:] + newlst[:length]
    return {arrayQ.dequeue for x in range(numofperm)}
