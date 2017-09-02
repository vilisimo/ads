class Queue:
    def __init__(self):
        self._items = []
        self._index = -1

    def enqueue(self, element):
        if element is None:
            raise TypeError("Element cannot be of type None")

        self._items.append(element)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("Empty queue cannot be dequeued")

        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyQueue("Empty queue cannot be peeked into")

        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        self._index = self._index + 1
        if self._index >= len(self._items):
            raise StopIteration

        return self._items[self._index]


class EmptyQueue(Exception):
    """ A wrapper exception to hide implementation details """
    pass
