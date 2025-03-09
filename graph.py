class Graph:
    def __init__(self):
        self.adj_list = []  # Список смежности: [[соседи_0], [соседи_1], ...]

    def add_vertex(self):
        """Добавляет новую вершину и возвращает её индекс."""
        self.adj_list.append([])
        return len(self.adj_list) - 1

    def add_edge(self, u, v):
        """Добавляет ребро между вершинами u и v (неориентированный граф)."""
        if u >= len(self.adj_list) or v >= len(self.adj_list):
            print("Ошибка: вершина не существует")
            return
        self.adj_list[u].append(v)
        if u != v:  # Избегаем дублирования для петель
            self.adj_list[v].append(u)

    def print_graph(self):
        """Выводит список смежности."""
        for i, neighbors in enumerate(self.adj_list):
            print(f"Вершина {i}: {neighbors}")

graph = Graph()
v0 = graph.add_vertex()  # Вершина 0
v1 = graph.add_vertex()  # Вершина 1
v2 = graph.add_vertex()  # Вершина 2

graph.add_edge(v0, v1)   # Ребро 0-1
graph.add_edge(v0, v2)   # Ребро 0-2

graph.print_graph()