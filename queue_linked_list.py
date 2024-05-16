class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if not self.front:
            self.front = self.rear = node(data)
        else:
            new_node = node(data)
            self.rear.next = new_node
            self.rear = new_node
        return self.display()

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def peek(self):
        if not self.front:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        cur_node = self.front
        queue_list = []
        while cur_node:
            queue_list.insert(0, cur_node.data)
            cur_node = cur_node.next
        return queue_list


def main():
    queue_test = queue()
    print(queue_test.peek())
    for i in [1, 2, 3, 4]:
        print(queue_test.enqueue(i))
    print("->", queue_test.display(), "->")
    print("dequeue", queue_test.dequeue())
    print("->", queue_test.display(), "->")
    print("peek", queue_test.peek())


main()
