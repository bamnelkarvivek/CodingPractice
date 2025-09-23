class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if not self.stack:
            return "Stack is empty."
        popped = self.stack.pop()
        return popped

    def peek(self):
        if not self.stack:
            return "Stack is empty."
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return " -> ".join(reversed([str(x) for x in self.stack]))+ " -> None"

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self,element):
        self.stack1.push(element)
    def dequeue(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()    
    def peek(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    
    def __str__(self):
        elements = self.stack2.stack[::-1] + self.stack1.stack
        return " <- ".join(str(element) for element in elements) if elements else "Queue is empty."
        
        

if __name__ == "__main__":
    q = QueueUsingStacks()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)   # 10 <- 20 <- 30

    print(q.dequeue())  # removes 10
    print(q)            # 20 <- 30

    q.enqueue(40)
    print(q)            # 20 <- 30 <- 40

    print(q.dequeue())  # removes 20
    print(q)            # 30 <- 40

    print(q.peek())     # front is 30