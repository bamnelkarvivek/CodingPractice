class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Getter methods
    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # Setter methods
    def set_value(self, value):
        self.value = value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class BST:
    def __init__(self):
        self.root = None

    # Insert method
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.get_value():
            if node.get_left() is None:
                node.set_left(Node(value))
            else:
                self._insert(node.get_left(), value)
        else:
            if node.get_right() is None:
                node.set_right(Node(value))
            else:
                self._insert(node.get_right(), value)

    # Search method
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.get_value() == value:
            return True
        elif value < node.get_value():
            return self._search(node.get_left(), value)
        else:
            return self._search(node.get_right(), value)

    # Public remove method
    def remove(self, value):
        if self.root is None:
            return "Empty Tree."
        self.root = self._remove(self.root, value)

    # Private recursive remove
    def _remove(self, node, value):
        if node is None:
            return None

        if value < node.get_value():
            node.set_left(self._remove(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self._remove(node.get_right(), value))
        else:
            # Case 1: No children
            if node.get_left() is None and node.get_right() is None:
                return None

            # Case 2: One child
            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()

            # Case 3: Two children
            successor = self._find_min(node.get_right())
            node.set_value(successor.get_value())
            node.set_right(self._remove(node.get_right(), successor.get_value()))

        return node

    def _find_min(self, node):
        while node.get_left() is not None:
            node = node.get_left()
        return node

    # Inorder traversal (sorted order)
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.get_left()) + [node.get_value()] + self._inorder(node.get_right())


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    bst = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Inorder before deletion:", bst.inorder())
    bst.remove(30)   # Case 3: node with two children
    print("Inorder after deleting 30:", bst.inorder())
    bst.remove(20)   # Case 1: leaf node
    print("Inorder after deleting 20:", bst.inorder())
    bst.remove(70)   # Case 2: one child
    print("Inorder after deleting 70:", bst.inorder())
