__author__ = 'Michael'

# Write a program to sort a stack in ascending order (with biggest items on top).
# You may use at most one additional stack to hold items, but you may not copy
# the elements into any other data structure (such as an array). The stack supports
# the following operations: push, pop, peek, and isEmpty.


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

    def peek(self):
        if self.head is None:
            return None

        return self.head.data


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

    sort(test_stack)
    print(test_stack)


# Horribly inefficient due to tons of recursion, but memory constraints in the question forced my hand.
def sort(the_stack):
    if the_stack is not None:
        if the_stack.count > 1:
            temp = the_stack.pop()
            sort(the_stack)
            insert(the_stack, temp)


def insert(the_stack, value):
    if the_stack.count == 0:
        the_stack.push(value)
    elif value < the_stack.peek():
        temp = the_stack.pop()
        insert(the_stack, value)
        the_stack.push(temp)
    else:
        the_stack.push(value)


def setup_test_stack():
    stack = Stack()

    for x in range(12):
        stack.push(x % 7)

    return stack


if __name__ == '__main__':
    main()