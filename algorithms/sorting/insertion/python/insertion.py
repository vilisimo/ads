def sort(items):
    if items is None:
        raise TypeError("Collection cannot be of type None")
    
    for index in range(1, len(items)):
        position = index
        value = items[index]

        while position > 0 and value < items[position-1]:
            items[position] = items[position-1]
            position -= 1
        
        # At this point position is already decremented,
        # hence higher value (previous item[position]) is not overwritten
        items[position] = value
