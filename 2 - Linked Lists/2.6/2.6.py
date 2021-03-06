__author__ = 'Michael'

# Given a corrupt linked list containing a loop, implement an algorithm which returns the node at
# the beginning of the loop.


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        if self.head is None:
            return ""

        temp = "[" + str(self.head) + "]"

        node = self.head.next

        while node is not None:
            temp += "->[" + str(node) + "]"
            node = node.next

        return temp

    def count(self):
        return self.count

    def add_to_head(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous(new_node)
            head = new_node
        self.count += 1

    def add_to_tail(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.count += 1

    def remove(self, node):
        if node.next is None:
            if node.previous is None:
                self.head = None
                self.tail = None
            else:
                self.tail = node.previous
                node.previous.next = None

        elif node.previous is None:
            if node.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
                node.next.previous = None

        else:
            temp = node.previous
            node.next.previous = temp
            temp.next = node.next

        self.count -= 1


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


def main():
    list_1, list_2 = setup_test_list()

    print(find_loop(list_1))
    print(find_loop(list_2))


def find_loop(linked_list):
    node = linked_list.head
    visited = []

    while node is not None:
        if visited.__contains__(node):
            return node.data

        visited.append(node)
        node = node.next

    return None


def setup_test_list():
    list_1 = LinkedList()

    for x in range(10):
        list_1.add_to_tail(Node(x % 7))

    node = list_1.tail
    node = node.previous

    node.next = list_1.head.next.next.next

    list_2 = LinkedList()

    for x in range(8):
        list_1.add_to_tail(Node(x % 3))

    return list_1, list_2

if __name__ == '__main__':
    main()