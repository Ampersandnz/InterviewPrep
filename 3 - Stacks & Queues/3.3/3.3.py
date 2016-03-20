__author__ = 'Michael'

# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
# and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack.
#
# Follow-up: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:
    def __init__(self, max_stack_size):
        self.the_stacks = [Stack()]
        self.stack_count = 1
        self.max_stack_size = max_stack_size

    def __str__(self):
        temp = self.the_stacks[0]

        for s in self.the_stacks[1:]:
            temp += '->' + str(s)

        return temp

    def count(self):
        return sum(s.count for s in self.the_stacks)

    def push(self, value):
        # TODO: If last stack is full, create new stack and increment stack count
        # TODO: Push to last stack
        pass

    def pop(self):
        # TODO: If last stack is empty, remove it and decrement stack count
        # TODO: Pop from last stack
        pass

    def pop_at(self, index):
        # TODO: Pop from specified stack
        # TODO: Possibly shuffle all elements down to fill the gap, possibly don't
        pass


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
    test_setofstacks = setup_test_setofstacks()
    print(test_setofstacks)

    print(test_setofstacks.pop())
    print(test_setofstacks.pop())

    print(test_setofstacks)

    print(test_setofstacks.pop_at(1))
    print(test_setofstacks.pop_at(1))
    print(test_setofstacks.pop_at(1))

    print(test_setofstacks)

    test_setofstacks.push("A")
    test_setofstacks.push("P")

    print(test_setofstacks)


def setup_test_setofstacks():
    stacks = SetOfStacks(5)

    for x in range(19):
        stacks.push(x % 7)

    return stacks


if __name__ == '__main__':
    main()