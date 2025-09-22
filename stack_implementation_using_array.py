class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
        print("Pushed: ",data)
    
    def pop(self):
        if not self.stack:
            return "Stack is empty."
        popped = self.stack.pop()
        print("Popped", popped)
        return popped

    def peek(self):
        if not self.stack:
            return "Stack is empty."
        return self.stack[-1]
    
    def __str__(self):
        return " -> ".join(reversed([str(x) for x in self.stack]))+ " -> None"
    
if __name__ == "__main__":
    mystack = Stack()
    mystack.push("Youtube")
    mystack.push("Google")
    mystack.push("Udemy")

    print(mystack)         # Youtube -> Google -> Udemy -> None
    print("Top:", mystack.peek())  # Udemy
    mystack.pop()  # Udemy
    print(mystack)         # Youtube -> Google -> None
