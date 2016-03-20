__author__ = 'Michael'

# An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures to maintain this system
# and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
# You may use the built-in LinkedList data structure


class Shelter:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue[::-1])

    def count(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue_any(self):
        return self.queue.pop()

    def dequeue_dog(self):
        return self.queue.pop()

    def dequeue_cat(self):
        return self.queue.pop()


def main():
    shelter = setup_shelter()

    print(shelter)


def setup_shelter():
    shelter = Shelter()

    shelter.enqueue('cat')
    shelter.enqueue('dog')

    return shelter

if __name__ == '__main__':
    main()