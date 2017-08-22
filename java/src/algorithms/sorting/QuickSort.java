package algorithms.sorting;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

import static helpers.ArrayMerger.mergeArrays;
import static java.util.Objects.requireNonNull;

public class QuickSort {

    private QuickSort() {
        throw new AssertionError("The class should not be instantiated");
    }

    /**
     * Note that due to generics this method only deals with strings, as
     * devising one that handles generic arrays is much more involved than
     * it should be for an algorithm that serves only as an example of
     * general principle (and has rather bad space complexity).
     */
    public static String[] sort(String[] items) {
        requireNonNull(items, "Collection should not be null");


        if (items.length < 2) {
            return items;
        }

        int pivot = ThreadLocalRandom.current().nextInt(0, items.length);

        List<String> lower = new ArrayList<>();
        List<String> higher = new ArrayList<>();

        for (int index = 0; index < items.length; index++) {
            if (index == pivot) {
                continue;
            }

            String currentItem = items[index];
            if (currentItem.compareTo(items[pivot]) > 0) {
                higher.add(items[index]);
            } else {
                lower.add(currentItem);
            }
        }

        String[] sortedLower = sort(lower.toArray(new String[0]));
        String[] pivotArray = new String[] {items[pivot]};
        String[] sortedHigher = sort(higher.toArray(new String[0]));
        String[] merged = mergeArrays(sortedLower, pivotArray, sortedHigher);

        return merged;
    }
}
