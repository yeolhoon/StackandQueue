class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = node(data)
        else:
            new_node = node(data)
            new_node.next = self.top
            self.top = new_node
        return None

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def main(self):
        self.push(1)
        self.push(2)
        self.push(3)
        self.push(4)
        data = self.peek()
        print(data)

stack_test = stack()
stack_test.main()