package algorithms.sorting;

import static helpers.Swapper.swap;
import static java.util.Objects.requireNonNull;

public class BubbleSort {
    public static <E extends Comparable<E>> void sort(E[] items) {
        requireNonNull(items, "Collection should not be null");

        int length = items.length;

        for (int outer = 0; outer < length - 1; outer++) {
            for (int inner = 0; inner < length - 1 - outer; inner++) {
                if (items[inner].compareTo(items[inner + 1]) > 0) {
                    swap(items, inner, inner + 1);
                }
            }
        }

    }
}