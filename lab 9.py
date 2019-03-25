class LinkedStack:
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

class Empty(Exception):
    pass
class LeakyStack:
    def __initi__(self,max_num):
        self.max = max_num
        self.data = []
    def __len__ (self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push (self, element):
        if len(self.data) >= self.max:
            self.data.append(element)
            self.data.pop(0)
    def pop(self):
        if is_empty():
            raise Empty("Empty")
        return self.data.pop()
    def top(self):
        if is_empty():
            raise Empty("Empty")
        return self.data[-1]
    def bottom(self):
        if is_empty():
            raise Empty("Empty")
        return self.data[0]


def sum_link_lists(link_list):
    if len(link_list) == 1:
        first = DoublyLinkedList.node.prev
        add = first.data
    else:
        res = link_list(len(link_list)-1)
        add += DoublyLinkedList.last_node
    return add

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
    def reverse_change_element_order(self):
        pointer1 = self.header.next
        pointer2 = self.trailer.prev
        counter = 0
        while counter < self.size//2:
            pointer1.data,pointer2.data = pointer2.data, pointer1.data
            pointer1 = pointer1.next
            pointer2 = pointer2.prev
            counter +=1
    def reverse_change_node_order(self):
        pointer1 = self.header.next
        pointer2 = self.trailer.prev
        counter = 0
        while counter < self.size//2:
            pointer1_prev = pointer1.prev
            pointer1_succ = pointer1.next
            pointer2_prev = ponter2.prev
            pointer2_succ = pointer2.next
            pointer1.data, pointer2.data = pointer2.data, pointer1.data
            pointer1_prev, pointer2_prev = pointer2_prev, pointer1_prev
            pointer1_succ, pointer2_succ = pointer2_succ, pointer1_succ
            pointe1 = pointer1.next
            pointer2 = pointer2.prev
            counter +=1
    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"


