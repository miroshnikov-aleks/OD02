class Tree:
    def __init__(self, root_value):
        self.root = [root_value]  # Корень дерева: [значение, дочерние_узлы...]

    def add_child(self, parent_value, value):
        """Добавляет дочерний узел с заданным значением к родительскому узлу."""
        def find_node(node):
            if node[0] == parent_value:
                return node
            for child in node[1:]:
                result = find_node(child)
                if result:
                    return result
            return None

        parent_node = find_node(self.root)
        if parent_node is not None:
            parent_node.append([value])
        else:
            print(f"Родительский узел {parent_value} не найден")

    def print_tree(self):
        """Выводит структуру дерева."""
        def print_node(node, level=0):
            print("  " * level + str(node[0]))
            for child in node[1:]:
                print_node(child, level + 1)
        print_node(self.root)

tree = Tree(1)          # Создаем корень со значением 1
tree.add_child(1, 2)    # Добавляем дочерний узел 2 к узлу 1
tree.add_child(1, 3)    # Добавляем дочерний узел 3 к узлу 1
tree.add_child(2, 4)    # Добавляем дочерний узел 4 к узлу 2
tree.print_tree()