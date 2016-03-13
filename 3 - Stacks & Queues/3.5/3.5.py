__author__ = 'Michael'

# Implement a MyQueue class which implements a queue using two stacks.


class MyQueue:
    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def __str__(self):
        while self.a.count > 0:
            self.b.push(self.b.pop())

        return str(self.b)

    def count(self):
        return self.a.count + self.b.count

    def enqueue(self, value):
        while self.a.count > 0:
            self.b.push(self.a.pop())

        self.b.push(value)

    def dequeue(self):
        while self.b.count > 0:
            self.a.push(self.b.pop())

        return self.a.pop()


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

        if self.head is None:
            self.tail = None
        else:
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
    test_queue = setup_test_queue()
    print(test_queue)

    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    (test_queue.enqueue("A"))
    (test_queue.enqueue("P"))
    print(test_queue)


def setup_test_queue():
    queue = MyQueue()

    for x in range(12):
        queue.enqueue(x % 7)

    return queue


if __name__ == '__main__':
    main()