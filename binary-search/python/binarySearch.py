def search(collection, element):
    if not collection or not element:
        raise TypeError("Arguments cannot be of type None")

    low = 0
    high = len(collection) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = collection[middle]
        
        if (guess == element):
            return middle
        elif (collection[middle] > element):
            high = middle - 1

        else: 
            low = middle + 1

    return -1