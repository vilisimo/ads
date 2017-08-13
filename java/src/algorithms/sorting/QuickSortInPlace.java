package algorithms.sorting;


import java.util.concurrent.ThreadLocalRandom;

/**
 * A quicksort implementation that takes (almost) no extra space.
 *
 * Although the logic is slightly more complex than {@link QuickSort},
 * the benefit is that generic collections can easily be sorted and
 * there is no need for extra data structures to store intermediate
 * results.
 */
public class QuickSortInPlace {
    public static <E extends Comparable<E>> void quicksort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection cannot be null");
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

        int head = start;
        int tail = end;

        E pivot = items[ThreadLocalRandom.current().nextInt(start, items.length)];

        while (head <= tail) {
            while (items[head].compareTo(pivot) < 0) {
                head++;
            }

            while (items[tail].compareTo(pivot) > 0) {
                tail--;
            }

            if (head <= tail) {
                E temp = items[head];
                items[head++] = items[tail];
                items[tail--] = temp;
            }
        }

        quicksort(items, start, tail);
        quicksort(items, head, end);
    }
}
