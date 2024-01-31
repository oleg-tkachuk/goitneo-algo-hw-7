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

    # Homework 7, task 1
    def find_max(self):
        return self._find_max_node(self.root)

    # Homework 7, task 1
    def _find_max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val

    # Homework 7, task 2
    def find_min(self):
        return self._find_min_node(self.root)

    # Homework 7, task 2
    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    # Homework 7, task 3
    def sum_of_values(self):
        return self._sum_of_values(self.root)

    # Homework 7, task 3
    def _sum_of_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_of_values(node.left) + self._sum_of_values(node.right)


# Demonstration of use
def main():
    random_from = 1
    random_to = 150
    number_of_values = 30

    print(f"Homework 7 - Task 1 | Create a binary search tree (BST)")
    bst = BST()

    print(f"Homework 7 - Task 1 | Generate {number_of_values} random values in the range from {random_from} to {random_to} and add them to the BST...")
    for _ in range(number_of_values):
        item = random.randint(1, 100)
        bst.insert(item)
        print(f"Homework 7 - Task 1 | Add value {item} to the BST")

    max_value = bst.find_max()
    print(f"Homework 7 - Task 1 | The maximum value in the BST is: {max_value}")

    max_value = bst.find_min()
    print(f"Homework 7 - Task 2 | The minimum value in the BST is: {max_value}")

    total_sum = bst.sum_of_values()
    print(f"Homework 7 - Task 3 | The sum of all values in the BST is: {total_sum}")

if __name__ == "__main__":
    main()