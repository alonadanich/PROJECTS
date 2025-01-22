"""
Завдання 3
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if not node:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def sum_of_tree(node):
    if node is None:
        return 0
    return node.value + sum_of_tree(node.left) + sum_of_tree(node.right)

if __name__ == "__main__":
    root = None
    values = [20, 10, 30, 5, 15, 25, 35]
    for value in values:
        root = insert(root, value)

    print("Сума всіх значень у дереві:", sum_of_tree(root))