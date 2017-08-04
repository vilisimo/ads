package algorithms.sorting.bubble.java;

public class BubbleSort {
    public static <E extends Comparable<E>> void sort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection cannot be null");
        }

        int length = items.length;

        for (int outer = 0; outer < length - 1; outer++) {
            for (int inner = 0; inner < length - 1 - outer; inner++) {
                if (items[inner].compareTo(items[inner + 1]) > 0) {
                    E temp = items[inner + 1];
                    items[inner + 1] = items[inner];
                    items[inner] = temp;
                }
            }
        }

    }
}
