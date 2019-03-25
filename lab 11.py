class BinaryTree:
    class Node:
        def __init__(self,data,left =None, right = None):
            self.data = data
            self.left = left
            self.parent = None
            self.right = right
    def __init(self, root=None):
        self.root = root
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0
    def subtree_count(self, curr_root): #using recursion to count
        if curr_root is None:
            return 0
        else:
            left_count = self.subtree_count(curr_root.left)
            right_count = self.subtree_count(curr_root.right)
            return left_count + right_count + 1
    def inverter(self):
        yield from self.inverter_maker(self.root)
    def inverter_maker(self,curr_root):
        if curr_root is None:
            return 0
        else:
            left = self.inverter_maker(curr_root.left)
            right = self.inverter_maker(curr_root.right)
            left,right = right,left
            yield curr_root
            yield from left
            yield from rightt
    def inversion_helper(self):
    def inversion(curr_root):
        if curr_root is None:   
            return
        inversion(curr_root.left)
        inversion(curr_root.right)
        curr_root.left, curr_root.right = curr_root.right, curr_root.left
    def subtree_children_dist(self, curr_root):
        leaf = 0
        single = 0
        double = 0
        if curr_root is None:
            return 0
        else:
            left_count = self.subtree_children_dist(curr_root.left)
            right_count = self.subtree_childen_dist(curr_root.right)
            if curr_root.left is None and curr_root.right is None:
                leaf += 1
                return leaf
            elif (curr_root.left is None and curr_root.right is not None) or (curr_root.left is not None and curr_root.right is None):
                single +=1
                return single
            else:
                double += 1
                return double
    def subtree_children_dist(self,curr_root):
        if curr_root is None:
            return [0,0,0]
        left = self.dist(curr_root.left)
        right = self.dist(curr_root.right)
        new_list = [left[i] + right[i] for i in range(3)]
        if curr_root.left is not None and curr_root.right is not None:
            new_list[2] += 1
        elif if curr_root.left is None and curr_root.right is None:
            new_list[1] += 1
        else:
            new_list[0] += 1
        return new_list

import doublylinkedlists
    def subtree_to_list(self,curr_root):
        curr_root.left
