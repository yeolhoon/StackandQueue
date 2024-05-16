class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
        return self.items

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def main():
    queue_array = queue()
    for i in [1, 2, 3, 4]:
        print(queue_array.enqueue(i))
    print("->", queue_array.items, "->")
    print("dequeue", queue_array.dequeue())
    print("->", queue_array.items, "->")
    print("peek", queue_array.peek())


main()