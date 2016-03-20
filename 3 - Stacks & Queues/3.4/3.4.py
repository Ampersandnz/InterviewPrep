__author__ = 'Michael'

# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes,
# which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom
# (i.e., each disk sits on top of an even larger one).
#
# You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk can only be placed on top of a larger disk.
#
# Write a program to move the disks from the first tower to the last using stacks


class Towers:
    def __init__(self):
        self.a = Stack()
        self.b = Stack()
        self.c = Stack()

    def __str__(self):
        return 'A): ' + str(self.a) + '\nB): ' + str(self.b) + '\nC): ' + str(self.c) + '\n'

    def recursive_move(self, disc, source, destination, other):
        if disc == 1:
            destination.push(source.pop())
        else:
            self.recursive_move(disc - 1, source, other, destination)
            destination.push(source.pop())
            self.recursive_move(disc - 1, other, destination, source)

    def solve(self):
        while self.a.count > 0 or self.b.count > 0:
            self.recursive_move(self.a.tail.data, self.a, self.c, self.b)


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        if self.count == 0:
            return ''
        elif self.count == 1:
            return '[' + str(self.head.data) + ']'
        else:
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
        if self.head is not None:
            return self.head.data
        else:
            return None


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


def main():
    towers = setup_towers(5)

    print(str(towers))

    towers.solve()

    print(str(towers))


def setup_towers(num):
    towers = Towers()

    while num:
        towers.a.push(num)
        num -= 1

    return towers


if __name__ == '__main__':
    main()