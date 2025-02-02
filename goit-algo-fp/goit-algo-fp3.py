"""
Завдання 3. Дерева, алгоритм Дейкстри
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph.edges}
    distances[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 6)
    graph.add_edge("C", "D", 3)

    start_vertex = "A"
    shortest_distances = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in shortest_distances.items():
        print(f"{vertex}: {distance}")