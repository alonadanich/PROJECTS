"""
Завдання 5. Візуалізація обходу бінарного дерева
Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
 Примітка. Використовуйте стек та чергу, НЕ рекурсію
"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    time.sleep(1)


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]
    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]

def generate_color(index, total):
    intensity = int(255 * (index / total))
    return f"#{intensity:02X}{(255-intensity):02X}00"

def bfs_traversal(root):
    if not root:
        return
    queue = [root]
    visited = set()
    index = 0
    total_nodes = 10

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            if node.id not in visited:
                node.color = generate_color(index, total_nodes)
                visited.add(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        draw_tree(root)
        index += 1

def dfs_traversal(root):
    if not root:
        return
    stack = [root]
    visited = set()
    index = 0
    total_nodes = 10

    while stack:
        node = stack.pop()
        if node.id not in visited:
            node.color = generate_color(index, total_nodes)
            draw_tree(root)
            visited.add(node.id)
            index += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

if __name__ == "__main__":
    heap = [10, 15, 20, 17, 25, 30, 35]
    heapq.heapify(heap)
    heap_tree = build_heap_tree(heap)
    print("Мін-купа:", heap)

    print("Обхід у глибину:")
    dfs_traversal(heap_tree)

    print("Обхід у ширину:")
    bfs_traversal(heap_tree)