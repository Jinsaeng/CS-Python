class Empty(Exception):
    pass
    
class MidStack:
    def __init__(self):
        self.data = []
        self.counter = 0
        self.front_ind = 0
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, val):
        self.data.append(val)
    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[0]
    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    def mid_push(self, elem):
        if (self.counter == len(self.data)):
            self.resize(2*len(self.data))
        if self.counter % 2 == 0:
            back_ind = (self.front_ind +self.counter) /2
        if self.counter % 2 == 1:
            back_ind == (self.front_ind +self.counter + 1) /2
        self.data[back_ind] = elem
        self.counter += 1
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(len(self)):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
