"""
Завдання 2
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.
"""
import networkx as nx
from collections import deque

G = nx.Graph()

G.add_nodes_from([
    "Центр. ринок", "1 школа", "Гот. 'Градецький'", "7 школа", 
    "ЦПКіВ", "Пед. універ.", "Політех. універ.", "Ринок 'Нива'", 
    "АТБ", "Епіцентр", "ТЦ Голівуд", "Дитяча лікарня", 
    "Рай. лікарня", "Красна площа"
])

G.add_edges_from([
    ("Центр. ринок", "1 школа"), 
    ("Центр. ринок", "Гот. 'Градецький'"), 
    ("Центр. ринок", "Красна площа"), 
    ("ЦПКіВ", "Пед. універ."), 
    ("ЦПКіВ", "Політех. універ."), 
    ("ЦПКіВ", "Красна площа"), 
    ("Красна площа", "Політех. універ."), 
    ("Ринок 'Нива'", "ТЦ Голівуд"), 
    ("Ринок 'Нива'", "Дитяча лікарня"),
    ("Ринок 'Нива'", "Пед. універ."),
    ("Ринок 'Нива'", "7 школа"),
    ("Ринок 'Нива'", "Епіцентр"),
    ("Політех. універ.", "Дитяча лікарня"), 
    ("Політех. універ.", "Рай. лікарня"), 
    ("Епіцентр", "Рай. лікарня"),
    ("Епіцентр", "ТЦ Голівуд"),
    ("Пед. універ.", "7 школа"),
    ("Гот. 'Градецький'", "1 школа"), 
    ("1 школа", "АТБ"),
    ("АТБ", "ТЦ Голівуд")
])

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

start_node = "7 школа"
goal_node = "Гот. 'Градецький'"

dfs_paths = list(dfs_path(G, start_node, goal_node))
print(f"Шляхи з {start_node} до {goal_node} за допомогою DFS:")
for path in dfs_paths:
    print(path)

bfs_paths = list(bfs_path(G, start_node, goal_node))
print(f"\nШляхи з {start_node} до {goal_node} за допомогою BFS:")
for path in bfs_paths:
    print(path)

print("\nВисновки:")
print("DFS шукає шлях, заглиблюючись у граф, і може знайти довші шляхи першими.")
print("BFS шукає шлях рівень за рівнем і завжди знаходить найкоротший шлях.")