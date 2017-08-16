package algorithms.sorting;

import static helpers.Swapper.swap;
import static java.util.Objects.requireNonNull;

public class SelectionSort {

    public static <E extends Comparable<E>> void sort(E[] items) {
        requireNonNull(items, "Collection should not be null");


        for (int index = 0; index < items.length - 1; index++) {
            int minIndex = index;
            for (int j = index + 1; j < items.length; j++) {
                if (items[minIndex].compareTo(items[j]) > 0) {
                    minIndex = j;
                }
            }

            if (minIndex != index) {
                swap(items, minIndex, index);
            }
        }

    }
}
