"""
Завдання 1
Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right

    return current.value

if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.right.right = TreeNode(40)

    print("Найбільше значення в дереві:", find_max_value(root))