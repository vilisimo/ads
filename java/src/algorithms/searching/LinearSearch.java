package algorithms.searching;

public class LinearSearch {
    public static <E> int search(E[] collection, E target) {
        if (collection == null || target == null) {
            throw new IllegalArgumentException("Arguments cannot be null");
        }

        for (int i = 0; i < collection.length; i++) {
            if (collection[i].equals(target)) {
                return i;
            }
        }

        return -1;
    }
}