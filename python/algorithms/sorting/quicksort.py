import random


def sort(items):
    if items is None:
        raise TypeError("Collection cannot be of type None")

    if len(items) < 2:
        return items

    pivot = random.randint(0, len(items) - 1)

    greater = []
    less = []

    for index in range(0, len(items)):
        if index == pivot:
            continue
        if items[index] > items[pivot]:
            greater.append(items[index])
        else:
            less.append(items[index])

    return sort(less) + [items[pivot]] + sort(greater)


def quicksort(items):
    """ In-place quicksort with random pivot """

    if items is None:
        raise TypeError("Collection cannot be of type None")

    _quicksort(items, 0, len(items) - 1)


def _quicksort(items, first, last):
    if first >= last:
        return

    if len(items) < 2:
        return

    pivot = items[random.randint(first, last)]
    head, tail = first, last

    while head <= tail:
        while items[head] < pivot:
            head += 1
        while items[tail] > pivot:
            tail -= 1

        if head <= tail:
            items[head], items[tail] = items[tail], items[head]
            head += 1
            tail -= 1

        _quicksort(items, first, tail)
        _quicksort(items, head, last)
