__author__ = 'Michael'

# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's digit is at the
# head of the list. Write a function that adds the two numbers and returns the sum
# as a linked list.

# Suppose the digits are stored in forward order. Repeat the above problem


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
    list_1, list_2 = setup_lists()
    print(list_1)
    print(list_2)

    print()

    sum_forwards = add_forwards(list_1, list_2)
    print(sum_forwards)

    sum_reverse = add_reverse(list_1, list_2)
    print(sum_reverse)


def add_forwards(list_1, list_2):
    node = list_1.head
    num_1 = 0

    while node is not None:
        num_1 *= 10
        num_1 += node.data
        node = node.next

    node = list_2.head
    num_2 = 0

    while node is not None:
        num_2 *= 10
        num_2 += node.data
        node = node.next

    sum_list = LinkedList()

    for char in str(num_1 + num_2):
        sum_list.add_to_tail(Node(int(char)))

    return sum_list

def add_reverse(list_1, list_2):
    node = list_1.head
    num_1 = 0
    i = 0

    while node is not None:
        num_1 += (node.data * pow(10, i))
        i += 1
        node = node.next

    node = list_2.head
    num_2 = 0
    i = 0

    while node is not None:
        num_2 += (node.data * pow(10, i))
        i += 1
        node = node.next

    sum_list = LinkedList()

    for char in str(num_1 + num_2):
        sum_list.add_to_tail(Node(int(char)))

    return sum_list


def setup_lists():
    list_1 = LinkedList()
    list_2 = LinkedList()

    for x in range(10):
        list_1.add_to_tail(Node(x % 7))

    for x in range(6):
        list_2.add_to_tail(Node(x % 3))

    return list_1, list_2

if __name__ == '__main__':
    main()