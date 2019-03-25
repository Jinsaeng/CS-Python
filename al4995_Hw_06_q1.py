class Empty(Exception):
    pass
    
class LinkedQueue:
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
        
    cap  = 10
    def __init__(self):
        self.data = [None] * ArrayQueue.cap
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
        self.data[back_ind] = self.DoublyLinkedList.add_before
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = self.DoublyLinkedList.delete_node
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
