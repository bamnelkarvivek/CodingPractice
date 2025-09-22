class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def set_data(self,data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def get_length(self):
        return self.length
    
    def peek(self):
        if self.top is None:
            return "Empty Stack"
        return self.top.get_data()
    
    def push(self,data):
        print("Pushed ",data)
        new_node = Node(data,self.top)
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return "Stack is empty."
        popped_data = self.top.get_data()
        print("Popped ",popped_data)
        self.top = self.top.get_next()
        self.length -= 1
        return popped_data

    def __str__(self):
        stack = []
        current_node = self.top
        while current_node:
            stack.append(str(current_node.get_data()))
            current_node = current_node.get_next()
        return " -> ".join(stack) + " -> None"
    
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("Google")
    my_stack.push("Youtube")
    my_stack.push("Udemy")

    print(my_stack)  
    # Udemy -> Youtube -> Google -> None

    print("Top Most item:", my_stack.peek())  
    print("Length of stack:", my_stack.get_length())    

    my_stack.pop()
    print(my_stack)  
    # Youtube -> Google -> None
