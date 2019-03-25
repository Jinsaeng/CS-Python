class CompactString:
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
    def __init__(self,orig_str):
        counter = 0
        for i in range(len(orig_str)):
            if orig_str[i] == orig_str[i+1]:
                letter = orig_str[i]
                counter += 1
            else:
                data = {letter: counter}
                letter = orig_str[i+1]
                counter = 0
            self.str = self.DoublyLinkedList.add_after(self.header, data)
    def __add__(self, other):
        for i in range(len(other)):
            item = other.DoublyLinkedList.delete_first()
            self.DoublyLinkedList.add_last(self.str.DoublyLinkedList.trailer.prev, item)
    def __lt__ (self, other):
        for i in range(len(self)):
            total_let_self = data[letter] + total_let
        for i in range(len(other)):
            total_let_other = data[letter] + total_let
        if total_let_self > total_let_other:
            return False
        else:
            return True
    def __le__(self,other):
        for i in range(len(self)):
            total_let_self = data[letter] + total_let
        for i in range(len(other)):
            total_let_other = data[letter] + total_let
        if total_let_self > total_let_other:
            return False
        else:
            return True
    def __gt__(self, other):
        for i in range(len(self)):
            total_let_self = data[letter] + total_let
        for i in range(len(other)):
            total_let_other = data[letter] + total_let
        if total_let_self > total_let_other:
            return True
        else:
            return False
    def __ge__(self, other):
        for i in range(len(self)):
            total_let_self = data[letter] + total_let
        for i in range(len(other)):
            total_let_other = data[letter] + total_let
        if total_let_self >= total_let_other:
            return True
        else:
            return False
    def __repr__ (self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"
