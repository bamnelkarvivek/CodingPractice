class Node:
    """A node in a doubly linked list"""
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next_node = next
        self.prev_node = prev

    def get_data(self):
        return self.data
    
    def set_data(self,d):
        self.data = d

    def get_next(self):
        return self.next_node
    
    def set_next(self,next):
        self.next_node = next

    def get_prev(self):
        return self.prev_node
    
    def set_prev(self,prev):
        self.prev_node = prev
        
class LinkedList:
    """A simple doubly linked list implementation."""
    def __init__(self,r = None):
        self.root = r
        self.size = 0

    def add(self,data):
        """Add a new node containing data to the head of the list."""
        new_node = Node(data, None, self.root)
        if self.root:
            self.root.set_prev(new_node)
        self.root = new_node
        self.size += 1

    def remove(self,d):
        """Remove the first node containing the specified data."""
        prev_node = None
        this_node = self.root
        next_node = None

        while this_node:
            next_node = this_node.get_next()
            if this_node.get_data() == d:
                if this_node.get_prev():
                    this_node.get_prev().set_next(this_node.get_next())
                else:
                    # Removing root
                    self.root = this_node.get_next()
                
                if this_node.get_next():
                    this_node.get_next().set_prev(this_node.get_prev())
                self.size -= 1
                return True
            this_node = this_node.get_next()
        return False
    
    def __str__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.root
        while current:
            nodes.append(str(current.get_data()))
            current = current.get_next()
        return " <-> ".join(nodes) if nodes else "Empty List"
    
    def __reversed__(self):
        """Return the string representation of the list in reverse order"""
        current = self.root
        if not current:
            return "Empty List"
        
        # Move to the tail
        while current.get_next():
            current = current.get_next()

        # Traverse backwards
        nodes = []
        while current:
            nodes.append(str(current.get_data()))
            current = current.get_prev()
        
        return " <-> ".join(nodes)
    
if __name__ == "__main__":
    #Example Usage
    ll = LinkedList()
    ll.add(5)
    ll.add(10)
    ll.add(15)

    print("Initial list:",ll) # Output: 15 <-> 10 <-> 5
    print("Size:",ll.size)    # Output: 3

    ll.remove(10)
    print("After removing 10:", ll) #Output: 15 <-> 5
    print("Size:",ll.size)          #Output: 2

    print("Reverse traversal:", reversed(ll))