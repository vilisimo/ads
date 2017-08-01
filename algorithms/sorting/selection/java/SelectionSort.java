package algorithms.sorting.selection.java;

public class SelectionSort {

    public static <E extends Comparable<E>> void sort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection cannot be null");
        }

        for (int index = 0; index < items.length - 1; index++) {
            int minIndex = index;
            for (int j = index + 1; j < items.length; j++) {
                if (items[minIndex].compareTo(items[j]) > 0) {
                    minIndex = j;
                }
            }

            if (minIndex != index) {
                E temp = items[index];
                items[index] = items[minIndex];
                items[minIndex] = temp;
            }
        }

    }
}