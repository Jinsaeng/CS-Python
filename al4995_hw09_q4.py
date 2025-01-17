#4
import random
class ChainingHashTableMap:
    class DoublyLinkedList:
        class Node:
            def __init__(self, data=None, prev=None, next=None):
                self.data = data
                self.prev = prev
                self.next = next

            def disconnect(self):
                self.data = None
                self.prev = None
                self.next = None


        def __init__(self):
            self.header = DoublyLinkedList.Node()
            self.trailer = DoublyLinkedList.Node()
            self.header.next = self.trailer
            self.trailer.prev = self.header
            self.size = 0

        def __len__(self):
            return self.size

        def is_empty(self):
            return len(self) == 0

        def first_node(self):
            if(self.is_empty()):
              raise Exception("List is empty")
            return self.header.next

        def last_node(self):
            if(self.is_empty()):
              raise Exception("List is empty")
            return self.trailer.prev

        def add_after(self, node, data):
            prev = node
            succ = node.next
            new_node = DoublyLinkedList.Node(data, prev, succ)
            prev.next = new_node
            succ.prev = new_node
            self.size += 1
            return new_node

        def add_first(self, data):
            return self.add_after(self.header, data)

        def add_last(self, data):
            return self.add_after(self.trailer.prev, data)

        def add_before(self, node, data):
            return self.add_after(node.prev, data)

        def delete_node(self, node):
            pred = node.prev
            succ = node.next
            pred.next = succ
            succ.prev = pred
            self.size -= 1
            data = node.data
            node.disconnect()
            return data

        def delete_first(self):
            if (self.is_empty()):
                raise Exception("List is empty")
            self.delete_node(self.first_node())

        def delete_last(self):
            if (self.is_empty()):
                raise Exception("List is empty")
            self.delete_node(self.last_node())

        def __iter__(self):
            if (self.is_empty()):
                return
            cursor = self.first_node()
            while cursor is not self.trailer:
                yield cursor.data
                cursor = cursor.next

        def __repr__(self):
            return "[" + " <--> ".join([str(item) for item in self]) + "]"
    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.table = []
        for i in range(N):
            self.table.append(DoublyLinkedList.DoublyLinkedList())
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)
        self.list = DoublyLinkedList.DoublyLinkedList()

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket.is_empty:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        old_size = len(self.table[i])
        if self.table[i].is_empty():
            self.table[i].DoublyLinkedList.add_first(value)
            self.list.add_first(value)
        else:
            self.table[i].DoubleLinkedList.add_after(key, value)
            self.list.add_after(key,value)
        new_size = len(self.table[i])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        curr_bucket.DoublyLinkedList.delete_node(currr_bucket[key])
        self.list.delete_node(key)
        self.n -= 1
        if curr_bucket.is_empty():
            self.table[i] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        return [key for key in self.list]

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value
