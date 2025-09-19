class Node:
    def __init__(self,d,n = None):
        self.data = d
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node = n
        
class LinkedList:
    def __init__(self,r = None):
        self.root = r
        self.size = 0
    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1
    def remove(self,d):
        prev_node = None
        this_node = self.root
        next_node = None
        while this_node:
            next_node = this_node.get_next()
            if this_node.get_data() == d:
                if prev_node == None:
                    self.root = next_node
                else:
                    prev_node.set_next(next_node)
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = next_node
        return False