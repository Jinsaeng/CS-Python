
class Empty(Exception):
    pass
class Queue:
    def __init__(self):
        self.data = []
        self.data2 = []
        self.num_of_elems = 0
        self.num_of_elems2 = 0
        self.front_ind = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return (self.num_of_elems == 0)
    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    def add_stack(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1
    def enqueue(self):
        for elem in range(self.num_of_elems):
            new = self.data.pop()
            self.data2.append(new)
            self.num_of_elems2 +=1
            if (self.num_of_elems == len(self.data2)):
                self.resize(2 * len(self.data2))
    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data2[self.front_ind]
        self.data2[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data2)
        self.num_of_elems2 -= 1
        if(self.num_of_elems2 < len(self.data2) // 4):
            self.resize(len(self.data2) // 2)
        return value
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
