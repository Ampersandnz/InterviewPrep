__author__ = 'Michael'

# Write code to partition a linked list around a value x, such that all nodes less than
# x come before all nodes greater than or equal to x.


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
    test_list = setup_test_list()
    print(test_list)

    test_list = sort(test_list)
    print(test_list)


def sort(linked_list):
    data = []

    node = linked_list.head

    while node is not None:
        data.append(node.data)
        node = node.next

    data.sort()

    sorted_list = LinkedList()

    for item in data:
        sorted_list.add_to_tail(Node(item))

    return sorted_list


def setup_test_list():
    test_list = LinkedList()

    for x in range(10):
        test_list.add_to_tail(Node(x % 7))

    return test_list

if __name__ == '__main__':
    main()