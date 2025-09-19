class Node:
    """A node in a singly linked list"""
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
    """A simple singly linked list implementation."""
    def __init__(self,r = None):
        self.root = r
        self.size = 0

    def add(self,d):
        """Add a new node containing data to the head of the list."""
        new_node = Node(d,self.root)
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
    
    def __str__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.root
        while current:
            nodes.append(str(current.get_data()))
            current = current.get_next()
        return " -> ".join(nodes) if nodes else "Empty List"
    
    def __reversed__(self):
        nodes = []
        current = self.root
        # iterate over the list
        while current:
            nodes.append(str(current.get_data()))
            current = current.get_next()
        return " -> ".join(reversed(nodes)) if nodes else "Empty list."

if __name__ == "__main__":
    #Example Usage
    ll = LinkedList()
    ll.add(5)
    ll.add(10)
    ll.add(15)

    print("Initial list:",ll) # Output: 15 -> 10 -> 5
    print("Size:",ll.size)    # Output: 3
    print("Reversed list:", reversed(ll)) # Output: 5 -> 10 -> 15

    ll.remove(10)
    print("After removing 10:", ll) #Output: 15 -> 5
    print("Size:",ll.size)          #Output: 2