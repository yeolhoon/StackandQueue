class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        return self.items

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def main(self):
        print(self.enqueue(1))
        print(self.enqueue(2))
        print(self.enqueue(3))
        print(self.enqueue(4))

        print(self.dequeue())
        print(self.peek())


queue_array = queue()
queue_array.main()