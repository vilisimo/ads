package algorithms.searching.recursive.binary.java;

/**
 * Note: for repeating numbers, this algorithm will not always find a first
 * occurrence. In order to make it so, one would need to include additional
 * steps to ensure that the found value is lower than the one before it, and,
 * if necessary, find the first repeating value (for example, iterating
 * backwards until it is found)
 * */
public class RecursiveBinarySearch {
    public static <E extends Comparable<E>> int search(E[] collection, E target) {
        if (collection == null || target == null) {
            throw new IllegalArgumentException("Arguments cannot be null");
        }

        int bottom = 0;
        int top = collection.length - 1;

        return recursiveSearch(collection, target, bottom, top);

    }

    private static <E extends Comparable<E>> int recursiveSearch(E[] collection, E target, int bottom, int top) {
        if (bottom > top) {
            return -1;
        }

        int middle = (bottom + top) / 2;

        if (collection[middle].compareTo(target) == 0) {
            return middle;
        } else if (collection[middle].compareTo(target) > 0) {
            return recursiveSearch(collection, target, bottom, middle - 1);
        } else {
            return recursiveSearch(collection, target, middle + 1, top);
        }
    }
}
