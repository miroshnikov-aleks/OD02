class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self.items = []

    def push(self, item):
        """Добавление элемента в стек."""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат последнего добавленного элемента."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Стек пуст.")

    def peek(self):
        """Просмотр последнего элемента без его удаления."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Стек пуст.")

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер стека."""
        return len(self.items)

# Пример работы со стеком
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Стек:", stack.items)  # Вывод: [10, 20, 30]
print("Верхний элемент стека:", stack.peek())  # Вывод: 30
print("Удаляем элемент:", stack.pop())  # Вывод: 30
print("Стек после удаления:", stack.items)  # Вывод: [10, 20]