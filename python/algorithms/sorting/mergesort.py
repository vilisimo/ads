def mergesort(items):
    if items is None:
        raise TypeError("Collection cannot be of type None")

    return sort(items)


def sort(items):
    if len(items) < 2:
        return items

    mid = len(items) // 2

    left = sort(items[:mid])
    right = sort(items[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_items = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_items.append(left[l])
            l += 1
        else:
            sorted_items.append(right[r])
            r += 1

    # Copy remaining members after we've iterated one list

    while l < len(left):
        sorted_items.append(left[l])
        l += 1

    while r < len(right):
        sorted_items.append(right[r])
        r += 1

    return sorted_items
