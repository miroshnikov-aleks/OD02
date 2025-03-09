class Queue:
    def __init__(self):
        """Инициализация пустой очереди."""
        self.items = []

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаление и возврат первого добавленного элемента."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Очередь пуста.")

    def peek(self):
        """Просмотр первого элемента без его удаления."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Очередь пуста.")

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер очереди."""
        return len(self.items)

# Пример работы с очередью
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Очередь:", queue.items)  # Вывод: [10, 20, 30]
print("Первый элемент очереди:", queue.peek())  # Вывод: 10
print("Удаляем элемент:", queue.dequeue())  # Вывод: 10
print("Очередь после удаления:", queue.items)  # Вывод: [20, 30]