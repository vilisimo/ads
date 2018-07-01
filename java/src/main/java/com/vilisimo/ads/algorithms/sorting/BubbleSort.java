package com.vilisimo.ads.algorithms.sorting;

import static com.vilisimo.ads.helpers.Comparer.greater;
import static com.vilisimo.ads.helpers.Swapper.swap;
import static java.util.Objects.requireNonNull;

public class BubbleSort {

    private BubbleSort() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E extends Comparable<E>> void sort(E[] items) {
        requireNonNull(items, "Collection should not be null");

        int length = items.length;

        for (int outer = 0; outer < length - 1; outer++) {
            for (int inner = 0; inner < length - 1 - outer; inner++) {
                if (greater(items[inner], items[inner + 1])) {
                    swap(items, inner, inner + 1);
                }
            }
        }
    }
}