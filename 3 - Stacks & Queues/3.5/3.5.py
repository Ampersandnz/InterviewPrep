__author__ = 'Michael'

# Write code to remove duplicates from an unsorted linked list


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        node = self.head.next
        temp = "[" + str(self.head.data) + "]"

        while node is not None:
            temp += "->[" + str(node) + "]"
            node = node.next

        return temp

    def count(self):
        return self.count

    def push(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

        self.count += 1

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = node.next
        self.head.previous = None

        self.count -= 1

        return node.data


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


def main():
    test_stack = setup_test_stack()
    print(test_stack)

    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack)


def setup_test_stack():
    stack = Stack()

    for x in range(10):
        stack.push(x % 7)

    return stack


if __name__ == '__main__':
    main()