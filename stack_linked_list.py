class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if not self.top:
            self.top = node(data)
        else:
            new_node = node(data)
            new_node.next = self.top
            self.top = new_node
        return self.display()

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        cur_node = self.top
        stack_list = []
        while cur_node:
            stack_list.append(cur_node.data)
            cur_node = cur_node.next
        return stack_list


def main():
    stack_test = stack()
    for i in [1, 2, 3, 4]:
        print(stack_test.push(i))
    print("<->", stack_test.display())
    print("pop", stack_test.pop())
    print("<->", stack_test.display())
    print("peek", stack_test.peek())


main()