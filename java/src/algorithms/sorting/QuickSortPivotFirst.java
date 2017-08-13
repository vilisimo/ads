package algorithms.sorting;

/**
 * In-place implementation of Quicksort.
 *
 * The implementation is rather similar to {@link QuickSortInPlace},
 * though the algorithm is simpler. This is due to the fact that pivot
 * is always chosen to be a first element in the collection. While it
 * makes the algorithm more intuitive and easier to understand, the
 * problem with such implementation is that recursion depth in case of
 * sorted collections can be n, where n is number of elements in the
 * collection.
 */
public class QuickSortPivotFirst {
    public static <E extends Comparable<E>> void quicksort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection should not be null");
        }

        if (items.length < 2) {
            return;
        }

        quicksort(items, 0, items.length - 1);
    }

    private static <E extends Comparable<E>> void quicksort(E[] items, int start, int end) {
        if (start >= end) {
            return;
        }

        int pivot = start;

        for (int i = start + 1; i <= end; i++) {
            if (items[start].compareTo(items[i]) > 0) {
                pivot++;
                E temp = items[i];
                items[i] = items[pivot];
                items[pivot] = temp;

            }
        }
        E temp = items[pivot];
        items[pivot] = items[start];
        items[start] = temp;

        quicksort(items, start, pivot - 1);
        quicksort(items, pivot + 1, end);
    }
}
