"""
Завдання 1
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.
Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).
"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Центр. ринок", "1 школа", "Гот. 'Градецький'", "7 школа", "ЦПКіВ", "Пед. універ.", "Політех. універ.", "Ринок 'Нива'", "АТБ", "Епіцентр", "ТЦ Голівуд", "Дитяча лікарня", "Рай. лікарня", "Красна площа"])

G.add_edges_from([("Центр. ринок", "1 школа"), 
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

pos = nx.spring_layout(G)
options = {
    "node_color": "lightblue",
    "edge_color": "yellow",
    "node_size": 2000,
    "node_shape": "o",
    "font_size": 8,
    "width": 3,
    "with_labels": True
}
nx.draw(G, pos=None, **options)
pos = nx.circular_layout(G)
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")

for node, degree in degree_dict.items():
    print(f" {node}: {degree}")

print("\nВисновки:")
print(f"Вузол з найбільшим ступенем: 'Ринок 'Нива'' (ступінь {degree_dict["Ринок 'Нива'"]})")
print(f"Середня ступінь вузлів: {sum(degree_dict.values()) / num_nodes}")

