import random


def sort(items):
    """
    Quicksort that has terrible space complexity. However, it demonstrates
    the main idea of quicksort nicely: find a pivot, find lower and higher
    elements than it, rinse and repeat.
    """

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
    """
    In-place quicksort with random pivot. Minimizes recursion depth in case of
    ordered collections.
    """

    if items is None:
        raise TypeError("Collection cannot be of type None")

    if len(items) < 2:
        return

    _quicksort(items, 0, len(items) - 1)


def _quicksort(items, first, last):
    if first >= last:
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


def qsort(items, first=0, last=None):
    """
    This version of quicksort always takes first element as a pivot.
    It allows to achieve sorting without relatively complex logic.
    """

    if items is None:
        raise TypeError("Collection cannot be of type None")

    if last is None:
        last = len(items) - 1

    if first >= last:
        return

    pivot = partition(items, first, last)
    qsort(items, first, pivot - 1)
    qsort(items, pivot + 1, last)


def partition(items, first, last):
    pivot_pos = first

    for index in range(first + 1, last + 1):
        if items[index] <= items[first]:
            pivot_pos += 1
            # We know that items[pivot_pos] > pivot value we're
            # comparing against, otherwise we would have switched it.
            # Therefore, we can freely switch it with pivot[index]
            items[index], items[pivot_pos] = items[pivot_pos], items[index]
    # We have kept our pivot value at items[first]. Now we need
    # to put it where it belongs (higher than all lower values)
    items[pivot_pos], items[first] = items[first], items[pivot_pos]

    return pivot_pos
