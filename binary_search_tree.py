class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value    
    def get_left(self):
        return self.left
    def set_left(self,value):
        self.left = value
    def get_right(self):
        return self.right
    def set_right(self,value):
        self.right = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None: # Tree is empty
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.get_value():
                if current_node.get_left() is None:
                    current_node.set_left(new_node)
                    return
                current_node = current_node.get_left()
            else:
                if current_node.get_right() is None:
                    current_node.set_right(new_node)
                    return
                current_node = current_node.get_right()
        
    def lookup(self,value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node is not None:
            if value == current_node.get_value():
                return True
            elif value < current_node.get_value():
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()
        return False
    
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        def traverse(current):
            if current:
                traverse(current.get_left())
                result.append(current.get_value())
                traverse(current.get_right())
        traverse(node)
        return result

    def __str__(self):
        # Display as sorted list
        return "BST: " + str(self.inorder_traversal())

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)

    print(bst.lookup(7))   # True
    print(bst.lookup(20))  # False
    print(bst)             # BST: [2, 5, 7, 10, 15]