# Note: for repeating numbers, this algorithm will not always find a first
# occurrence. In order to make it so, one would need to include additional
# steps to ensure that the found value is lower than the one before it, and,
# if necessary, find the first repeating value (for example, iterating
# backwards until it is found)


def search(collection, target) -> int:
  if collection is None or not target:
    raise TypeError("Arguments cannot be of type None")

  start, end = 0, len(collection) - 1

  while start <= end:
    mid = (start + end) // 2
    if (collection[mid] == target):
      return mid
    if (collection[mid] < target):
      start = mid + 1
    else:
      end = mid - 1
  return -1
