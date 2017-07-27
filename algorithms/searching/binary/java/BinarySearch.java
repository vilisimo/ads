package algorithms.searching.binary.java;

public class BinarySearch {
    public static <E extends Comparable<E>> int search(E[] collection, E target) {
        if (collection == null || target == null) {
            throw new IllegalArgumentException("Arguments cannot be null");
        }

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