def search(collection, target):
    if collection is None or not target:
        raise TypeError("Arguments cannot be of type None")

    for index, element in enumerate(collection):
        if element == target:
            return index

    return -1;