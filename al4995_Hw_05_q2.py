class Empty(Exception):
    pass
class MaxStack:
    def __init__(self):
        self.data = []
        self.front_ind = 0
        self.max = 0
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.data)
    def push(self, val):
        self.data.append(val)
        self.max()
    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[0]
    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    def max(self):
        if (self.is_empty()):
            raise Empty("MaxS is empty")
        if self.val > self.max:
            self.max = self.val
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(len(self)):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
