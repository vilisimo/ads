package algorithms.searching;

import static java.util.Objects.requireNonNull;

public class LinearSearch {

    private LinearSearch() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E> int search(E[] collection, E target) {
        requireNonNull(collection, "Collection should not be null");
        requireNonNull(target, "Target object should not be null");

        for (int i = 0; i < collection.length; i++) {
            if (collection[i].equals(target)) {
                return i;
            }
        }

        return -1;
    }
}