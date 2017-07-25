# Note: for repeating numbers, this algorithm will not
# always be correct. In order to make it so, one would
# need to include additional steps to ensure that the
# found value is lower than the one before it, and, if
# necessary, find the first repeating value (for example,
# iterating backwards until it is found)

def search(collection, target):
    try:
        if len(collection) == 0:
            return -1
    except TypeError:
        raise TypeError("Arguments cannot be of type None")
    
    if not target:
        raise TypeError("Arguments cannot be of type None")  

    low = 0
    high = len(collection) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = collection[middle]
        
        if (guess == target):
            return middle
        elif (collection[middle] > target):
            high = middle - 1

        else: 
            low = middle + 1

    return -1

def search(collection, target):
    try:
        if len(collection) == 0:
            return -1
    except TypeError:
        raise TypeError("Arguments cannot be of type None")

    if not target:
        raise TypeError("Arguments cannot be of type None")    
        
    bottom = 0
    top = len(collection) - 1

    return recursive_search(collection, bottom, top, target)


def recursive_search(collection, bottom, top, target):
    mid = (bottom + top) // 2

    if bottom > top:
        return -1
    elif collection[mid] == target:
        return mid;
    elif collection[mid] > target:
        return recursive_search(collection, bottom, mid - 1, target)
    else:
        return recursive_search(collection, mid + 1, top, target)
