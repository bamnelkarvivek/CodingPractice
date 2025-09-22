class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):   # fixed
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class Queue:
    """Queue implementation using linked list (FIFO)"""

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """Returns the element at the front of the queue"""
        if self.first is None:
            return None
        return self.first.get_data()

    def enqueue(self, element):
        """Adds an element to the back of the queue"""
        new_node = Node(element)
        if self.last:  # queue is not empty
            self.last.set_next(new_node)
        self.last = new_node
        if self.first is None:  # queue was empty
            self.first = new_node
        self.length += 1

    def dequeue(self):
        """Removes and returns the element from the front of the queue"""
        if self.first is None:
            return None
        removed_element = self.first.get_data()
        self.first = self.first.get_next()
        if self.first is None:  # queue became empty
            self.last = None
        self.length -= 1
        return removed_element

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.first
        nodes = []
        while current:
            nodes.append(str(current.get_data()))
            current = current.get_next()
        return " <- ".join(nodes)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)            # 10 <- 20 <- 30
    print(q.peek())     # 10
    print(q.dequeue())  # 10
    print(q)            # 20 <- 30
    print(len(q))       # 2
