class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    # Добавление ребра между двумя вершинами
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Печать графа
    def print_graph(self):
        for i in range(self.V):
            print(f"Вершина {i}: ", end="")
            for neighbor in self.adj_list[i]:
                print(f"{neighbor}", end=" ")
            print()

# Создаем граф с 5 вершинами
graph = Graph(5)

# Добавляем ребра
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Печать графа
graph.print_graph()