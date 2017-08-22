package algorithms.sorting;

import static helpers.Comparer.greater;
import static java.util.Objects.requireNonNull;

public class InsertionSort {

    private InsertionSort() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E extends Comparable<E>> void sort(E[] items) {
        requireNonNull(items, "Collection should not be null");

        for (int index = 1; index < items.length; index++) {
            int currPos = index;
            E value = items[index];

            while (currPos > 0 && greater(items[currPos-1], value)) {
                items[currPos] = items[currPos-1];
                currPos--;
            }
            items[currPos] = value;
        }
    }
}
