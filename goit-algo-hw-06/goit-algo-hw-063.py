"""
Завдання 3
Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
"""
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_nodes_from([
    "Центр. ринок", "1 школа", "Гот. 'Градецький'", "7 школа", 
    "ЦПКіВ", "Пед. універ.", "Політех. універ.", "Ринок 'Нива'", 
    "АТБ", "Епіцентр", "ТЦ Голівуд", "Дитяча лікарня", 
    "Рай. лікарня", "Красна площа"
])

G.add_edges_from([
    ("Центр. ринок", "1 школа", {"weight": 1}), 
    ("Центр. ринок", "Гот. 'Градецький'", {"weight": 2}), 
    ("Центр. ринок", "Красна площа", {"weight": 3}), 
    ("ЦПКіВ", "Пед. універ.", {"weight": 1}), 
    ("ЦПКіВ", "Політех. універ.", {"weight": 3}), 
    ("ЦПКіВ", "Красна площа", {"weight": 5}), 
    ("Красна площа", "Політех. універ.", {"weight": 6}), 
    ("Ринок 'Нива'", "ТЦ Голівуд", {"weight": 2}), 
    ("Ринок 'Нива'", "Дитяча лікарня", {"weight": 1}),
    ("Ринок 'Нива'", "Пед. універ.", {"weight": 2}),
    ("Ринок 'Нива'", "7 школа", {"weight": 1}),
    ("Ринок 'Нива'", "Епіцентр", {"weight": 2}),
    ("Політех. універ.", "Дитяча лікарня", {"weight": 2}), 
    ("Політех. універ.", "Рай. лікарня", {"weight": 1}), 
    ("Епіцентр", "Рай. лікарня", {"weight": 3}),
    ("Епіцентр", "ТЦ Голівуд", {"weight": 2}),
    ("Пед. універ.", "7 школа", {"weight": 2}),
    ("Гот. 'Градецький'", "1 школа", {"weight": 2}), 
    ("1 школа", "АТБ", {"weight": 1}),
    ("АТБ", "ТЦ Голівуд", {"weight": 2})
])


options = {
    "node_color": "lightblue",
    "edge_color": "yellow",
    "node_size": 2000,
    "node_shape": "o",
    "font_size": 8,
    "width": 3,
    "with_labels": True
}

pos = nx.kamada_kawai_layout(G, weight="weight")
nx.draw(G, pos, **options)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")


all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G))

for source, target_dict in all_pairs_shortest_paths.items():
    for target, length in target_dict.items():
        print(f"Найкоротший шлях від '{source}' до '{target}' має довжину {length}")
        

plt.show()     
