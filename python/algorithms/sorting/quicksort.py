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
