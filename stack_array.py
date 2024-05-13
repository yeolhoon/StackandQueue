class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def main(self):
        print(self.push(1))
        print(self.push(2))
        print(self.push(3))
        print(self.push(4))

        print(self.pop())
        print(self.peek())


stack_array = stack()
stack_array.main()
