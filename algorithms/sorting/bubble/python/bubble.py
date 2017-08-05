def sort(items):
    if items is None:
        raise TypeError("Collection cannot be of type None")

    length = len(items)

    for outer in range(length - 1):
        for inner in range(length - 1 - outer):
            if items[inner] > items[inner + 1]:
                items[inner], items[inner + 1] = items[inner + 1], items[inner]
