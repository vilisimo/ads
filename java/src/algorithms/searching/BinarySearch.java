package algorithms.searching;

import static java.util.Objects.requireNonNull;

/**
 * Note: for repeating numbers, this algorithm will not always find a first
 * occurrence. In order to make it so, one would need to include additional
 * steps to ensure that the found value is lower than the one before it, and,
 * if necessary, find the first repeating value (for example, iterating
 * backwards until it is found)
 * */
public class BinarySearch {

    private BinarySearch() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E extends Comparable<E>> int search(E[] collection, E target) {
        requireNonNull(collection, "Collection should not be null");
        requireNonNull(target, "Target object should not be null");

        int bottom = 0;
        int top = collection.length - 1;

        while (bottom <= top) {
            int mid = (top + bottom) / 2;
            if (collection[mid].compareTo(target) == 0) {
                return mid;
            } else if (collection[mid].compareTo(target) > 0) {
                top = mid -1;
            } else {
                bottom = mid + 1;
            }
        }

        return -1;
    }
}