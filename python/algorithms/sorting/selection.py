def sort(items):
    if items is None:
        raise TypeError("Arguments cannot be of type None")

    for index in range(len(items)):
        min_index = index

        for inner_index in range(index + 1, len(items)):
            if items[inner_index] < items[min_index]:
                min_index = inner_index

        if min_index != index:
            items[index], items[min_index] = items[min_index], items[index]
