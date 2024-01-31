import random
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def find_max(self):
        return self._find_max_node(self.root)

    def _find_max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val

# Demonstration of use
def main():
    random_from = 1
    random_to = 150
    print(f"Homework 7 - Task 1 | Create a binary search tree (BST)")
    bst = BST()

    print(f"Homework 7 - Task 1 | Generate 30 random values in the range from {random_from} to {random_to} and add them to the BST...")
    for _ in range(0, 30):
        item = random.randint(1, 100)
        bst.insert(item)
        print(f"Homework 7 - Task 1 | Add value {item} to the BST")

    max_value = bst.find_max()
    print(f"Homework 7 - Task 1 | The maximum value in the binary search tree is: {max_value}")

if __name__ == "__main__":
    main()