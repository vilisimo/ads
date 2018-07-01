package com.vilisimo.ads.algorithms.sorting;

import static com.vilisimo.ads.helpers.Comparer.greater;
import static java.util.Objects.requireNonNull;

public class MergeSort {

    private MergeSort() {
        throw new AssertionError("The class should not be instantiated");
    }

    /**
     * The method simply serves as a facade that hides complexity
     * from the user. Real work happens in the private methods.
     */
    @SuppressWarnings("unchecked")
    public static <E extends Comparable<E>> void mergeSort(E[] toSort) {
        requireNonNull(toSort, "Collection should not be null");

        if (toSort.length < 2) {
            return;
        }

        E[] temp = (E[]) new Comparable[toSort.length];
        sort(toSort, temp, 0, toSort.length - 1);
    }

    /**
     * Although the method is conveniently called "sort", all it does is
     * splits arrays into halves, and instructs the other method to sort them.
     * Hence, this kind of Merge Sort might in fact be more understandable if
     * named something along the lines of Split Sort.
     */
    private static <E extends Comparable<E>> void sort(E[] toSort, E[] temp, int first, int last) {
        if (first >= last) {
            return;
        }

        int mid = first + (last - first) / 2;

        sort(toSort, temp, first, mid);
        sort(toSort, temp, mid + 1, last);
        merge(toSort, temp, first, mid, last);
    }

    /**
     * Although the method is conventionally named as "merge", in fact it is
     * more of a sort. It simply rearranges two halves of an array so that
     * the elements are in ascending order. There are no two entities that
     * are merged together. Rather, one entity's members are rearranged.
     */
    private static <E extends Comparable<E>> void merge(E[] toSort, E[] temp, int first, int mid, int last) {
        System.arraycopy(toSort, first, temp, first, last + 1 - first);

        int firstIdx = first; // beginning of first half
        int secondIdx = mid + 1; // beginning of second half
        for (int k = first;  k <= last; k++) {
            if (firstIdx > mid) {
                // we copied all elements from first half, so finish merging
                toSort[k] = temp[secondIdx++];
            } else if (secondIdx > last) {
                // we copied all elements from second half, so finish merging
                toSort[k] = temp[firstIdx++];
            }
            else if (greater(temp[firstIdx], temp[secondIdx])) {
                toSort[k] = temp[secondIdx++];
            } else {
                toSort[k] = temp[firstIdx++];
            }
        }
    }
}