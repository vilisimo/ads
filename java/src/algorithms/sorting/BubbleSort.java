package algorithms.sorting;

import static helpers.Swapper.swap;

public class BubbleSort {
    public static <E extends Comparable<E>> void sort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection cannot be null");
        }

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