class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = node(data)
        else:
            new_node = node(data)
            self.rear.next = new_node
            self.rear = new_node
        return None

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def main(self):
        for i in [1, 2, 3, 4]:
            self.enqueue(i)
        data = self.dequeue()
        peek_data = self.peek()
        print(data)
        print(peek_data)


queue_test = queue()
queue_test.main()