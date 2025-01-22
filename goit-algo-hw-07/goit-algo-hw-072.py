"""
Завдання 2
Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(node, value):
    if not node:
        return Node(value)
    elif value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and value < node.left.value:
        return rotate_right(node)
    
    if balance < -1 and value > node.right.value:
        return rotate_left(node)
    
    if balance > 1 and value > node.left.value:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    
    if balance < -1 and value < node.right.value:
        node.right = rotate_right(node.right)
        return rotate_left(node)
    
    return node

def find_min_value(node):
    if node is None:
        print("Дерево порожнє.")
        return None
    
    current = node
    while current.left is not None:
        current = current.left
    return current.value

if __name__ == "__main__":
    root = None
    values = [20, 10, 30, 5, 15, 25, 35]
    for value in values:
        root = insert(root, value)

    print("Найменше значення в дереві:", find_min_value(root))

# empty_tree = None 
# print("Найменше значення в порожньому дереві:", find_min_value(empty_tree))