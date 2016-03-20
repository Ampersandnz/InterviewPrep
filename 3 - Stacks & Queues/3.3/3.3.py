__author__ = 'Michael'

# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
# and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack.
#
# Follow-up: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:
    default_stack_size = 25

    def __init__(self, max_stack_size):
        # Set a default value when the number supplied by the user is invalid
        if type(max_stack_size) is not int or max_stack_size < 1:
            max_stack_size = self.default_stack_size
        self.the_stacks = [Stack()]
        self.max_stack_size = max_stack_size

    def __str__(self):
        if len(self.the_stacks) == 0:
            return ''
        elif len(self.the_stacks) == 1:
            return str(self.the_stacks[0])
        elif len(self.the_stacks) == 2:
            return str(self.the_stacks[1]) + '->' + str(self.the_stacks[0])
        else:
            temp = ''
            for s in self.the_stacks[-2::-1]:
                temp += '->' + str(s)

            temp = str(self.the_stacks[-1]) + temp

            return temp

    def count(self):
        return sum(s.count for s in self.the_stacks)

    def push(self, value):
        if self.the_stacks[-1].count == self.max_stack_size:
            self.the_stacks.append(Stack())

        self.the_stacks[-1].push(value)

    def pop(self):
        if self.the_stacks[-1].count == 0:
            self.the_stacks.pop()

        if len(self.the_stacks) == 0:
            return None
        else:
            return self.the_stacks[-1].pop()

    def pop_at(self, index):
        if len(self.the_stacks) == 0:
            return None

        if index >= len(self.the_stacks) or index < 0:
            return None

        if index == len(self.the_stacks) - 1 and self.the_stacks[-1].count == 0:
            return None

        the_value = self.the_stacks[index].pop()

        temp = []

        # It's probably much more efficient to manually move all the nodes around between the stacks but this is much
        # easier to conceptualise/write.
        for s in self.the_stacks[-1:index:-1]:
            while s.count > 0:
                temp.append(s.pop())
            self.the_stacks.pop()

        while len(temp) > 0:
            self.push(temp.pop())

        return the_value


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
    stacks = SetOfStacks(3)

    for x in range(19):
        stacks.push(x % 7)

    return stacks


if __name__ == '__main__':
    main()