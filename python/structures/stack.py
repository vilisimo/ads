class Stack:
    def __init__(self):
        self._items = []
        self._index = 0

    def push(self, item):
        if item is None:
            raise TypeError("Element cannot be of type None")

        self._items.append(item)
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be popped")
        self._index -= 1

        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStack("Empty stack cannot be peeked into")

        return self._items[self._index - 1]

    def is_empty(self):
        return self._index <= 0

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index = self._index - 1

        return self._items[self._index]


class EmptyStack(Exception):
    """ A wrapper exception to hide implementation details """
    pass
