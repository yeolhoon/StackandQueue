class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)
        return self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

def main():
    stack_array = stack()
    for i in [1, 2, 3, 4]:
        print(stack_array.push(i))

    print("<->", stack_array.items)
    print("pop", stack_array.pop())
    print("<->", stack_array.items)
    print("peek", stack_array.peek())


main()
