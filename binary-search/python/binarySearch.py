# Note: for repeating numbers, this algorithm will not
# always be correct. In order to make it so, one would
# need to include additional steps to ensure that the
# found value is lower than the one before it, and, if
# necessary, find the first repeating value (for example,
# iterating backwards until it is found)

def search(collection, target):
    if collection is None or not target:
        raise TypeError("Arguments cannot be of type None")
    if len(collection) == 0:
        return -1

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