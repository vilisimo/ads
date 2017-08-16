package helpers;

import static java.util.Objects.requireNonNull;

/**
 * Swaps two elements in an array.
 *
 * First element becomes the second and the second becomes the first.
 */
public class Swapper {
    public static <E> void swap(E[] items, int first, int second) {
        requireNonNull(items, "Collection should not be null");

        if (first >= items.length || second >= items.length) {
            throw new ArrayIndexOutOfBoundsException("Indices cannot be larger than the size of array");
        }

        if (first < 0 || second < 0) {
            throw new ArrayIndexOutOfBoundsException("Indices cannot be lower than 0");
        }

        if (first == second) {
            return;
        }

        E temp = items[first];
        items[first] = items[second];
        items[second] = temp;
    }
}
