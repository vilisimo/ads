package com.vilisimo.ads.algorithms.sorting;

import static com.vilisimo.ads.helpers.Comparer.greater;
import static com.vilisimo.ads.helpers.Swapper.swap;
import static java.util.Objects.requireNonNull;

public class SelectionSort {

    private SelectionSort() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E extends Comparable<E>> void sort(E[] items) {
        requireNonNull(items, "Collection should not be null");


        for (int index = 0; index < items.length - 1; index++) {
            int minIndex = index;
            for (int j = index + 1; j < items.length; j++) {
                if (greater(items[minIndex], items[j])) {
                    minIndex = j;
                }
            }

            if (minIndex != index) {
                swap(items, minIndex, index);
            }
        }
    }
}
