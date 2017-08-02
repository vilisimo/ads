package algorithms.sorting.insertion.java;

public class InsertionSort {
    public static <E extends Comparable<E>> void sort(E[] items) {
        if (items == null) {
            throw new IllegalArgumentException("Collection cannot be null");
        }

        for (int index = 1; index < items.length; index++) {
            int currPos = index;
            E value = items[index];

            while (currPos > 0 && value.compareTo(items[currPos-1]) < 0) {
                items[currPos] = items[currPos-1];
                currPos--;
            }
            items[currPos] = value;
        }
    }
}