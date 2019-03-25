
class Empty(Exception):
    pass
    
class ArrayDeque:
    
    def __init__(self):
        self.front_ind = 0
        self.num_of_elems = 0
        
    def __len__(self):
        return self.num_of_elems
    
    def is_empty(self):
        if self.num_of_elems == 0:
            return True
        else:
            return False
        
    def first(self):
        return self.data[front_ind]
    
    def last(self):
        return self.data[back_ind]
    
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
    
    def add_first(self, elem):
        if(self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1

    def add_last(self, e):
        if(self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = elem
        self.num_of_elems += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
        
class BoostArrayQueue:
    
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

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

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

    def boost(self, k):
        if k <= self.num_of_elems:
            for ele in range(k,self.num_of_elems):
                self.data[ele+1] = self.data[ele]
            self.data[self.num_of_elems - k] = self.data[self.num_of_elems-1]
        elif k > self.num_of_elems:
            for ele in range(self.num_of_elems):
                self.data[ele+1] = self.data[ele]
            self.data[0] = self.data[self.num_of_elems-1]
    def boost(self,k):
        data = self.queue.data
        back = (self.queue.front_ind + self.queue.num_of_elements-1) % len(data)
        if k >= len(self):
            k = len(self) -1
            for i in range(k):
                before_back = (back-1) % len(data)
            data[back], data[before_back] = data[before_back], data[back]




def nested_counter(lst):
    total = 0
    minitotal = 0 
    for ele in lst:
        while isinstance(ele,list):
            if len(ele) == 1:
                total += ele[0]
            elif len(ele) > 1:
                for item in range(len(ele)):
                    if isinstance(item,int):
                        total += item
                    elif isinstance(item,list):
                        ele = item
        total += ele
    return total
def nested_counter(lst):
    total = 0
    ind = 0
    flag = True
    Q = ArrayQueue.ArrayQueue()
    while flag:
        if isinstance(lst[ind]), list

print(nested_counter([1,[2,3],[2],6]))

