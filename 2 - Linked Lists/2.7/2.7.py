__author__ = 'Michael'

# Implement a function to check if a linked list is a palindrome.


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
    test_list_1, test_list_2 = setup_test_lists()
    print(test_list_1)
    print(is_palindrome(test_list_1))

    print(test_list_2)
    print(is_palindrome(test_list_2))


def is_palindrome(linked_list):
    node = linked_list.head
    array = []

    while node is not None:
        array.append(node.data)
        node = node.next

    forwards = "".join(str(x) for x in array)
    reverse = "".join(str(x) for x in array)[::-1]

    return forwards == reverse


def setup_test_lists():
    list_1 = LinkedList()

    for x in range(10):
        list_1.add_to_tail(Node(x % 7))

    list_2 = LinkedList()
    list_2.add_to_tail(Node("a"))
    list_2.add_to_tail(Node("a"))
    list_2.add_to_tail(Node("b"))
    list_2.add_to_tail(Node("a"))
    list_2.add_to_tail(Node("a"))

    return list_1, list_2

if __name__ == '__main__':
    main()