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
        return str(self.queue)

    def count(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue_any(self):
        return self.queue.pop(0)

    def dequeue_dog(self):
        try:
            index = self.queue.index('dog')
        except ValueError:
            return

        return self.queue.pop(index)

    def dequeue_cat(self):
        try:
            index = self.queue.index('cat')
        except ValueError:
            return

        return self.queue.pop(index)


def main():
    shelter = setup_shelter()

    print(shelter)

    shelter.dequeue_cat()
    shelter.dequeue_cat()

    print(shelter)

    shelter.dequeue_any()
    shelter.dequeue_any()
    shelter.dequeue_any()

    shelter.dequeue_cat()

    print(shelter)

    shelter.dequeue_dog()

    print(shelter)


def setup_shelter():
    shelter = Shelter()

    shelter.enqueue('cat')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')

    return shelter

if __name__ == '__main__':
    main()