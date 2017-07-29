# Note: for repeating numbers, this algorithm will not always find a first
# occurrence. In order to make it so, one would need to include additional
# steps to ensure that the found value is lower than the one before it, and,
# if necessary, find the first repeating value (for example, iterating
# backwards until it is found)

def search(collection, target):
    if collection is None or not target:
        raise TypeError("Arguments cannot be of type None")
        
    bottom = 0
    top = len(collection) - 1

    return recursive_search(collection, bottom, top, target)


def recursive_search(collection, bottom, top, target):
    if bottom > top:
        return -1

    mid = (bottom + top) // 2

    if collection[mid] == target:
        return mid;
    elif collection[mid] > target:
        return recursive_search(collection, bottom, mid - 1, target)
    else:
        return recursive_search(collection, mid + 1, top, target)
