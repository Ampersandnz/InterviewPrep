__author__ = 'Michael'

# Basic linked list implementation


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous(new_node)
            head = new_node

    def add_to_tail(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


def main():
    test_list = LinkedList()
    test_node = Node("blah")
    test_list.add_to_head(test_node)

    print(test_node)
    print(test_list.head)


if __name__ == '__main__':
    main()