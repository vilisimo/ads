package helpers;

/**
 * Swaps two elements in an array.
 *
 * First element becomes the second and the second becomes the first.
 */
public class Swapper {
    public static <E> void swap(E[] items, int first, int second) {
        if (items == null) {
            throw new IllegalArgumentException("Collection should not be null");
        }

        if (first == second) {
            return;
        }

        E temp = items[first];
        items[first] = items[second];
        items[second] = temp;
    }
}
