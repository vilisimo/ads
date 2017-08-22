package algorithms.sorting;

import helpers.Contrived;
import org.junit.Test;

import static algorithms.sorting.MergeSort.mergeSort;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class MergeSortTest {

    @Test
    public void sortsCollection() {
        String[] items = {"d", "z", "a"};
        String[] expected = {"a", "d", "z"};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithEdgeCases() {
        Integer[] items = {1, 1, -3, 1, 13, 9};
        Integer[] expected = {-3, 1, 1, 1, 9, 13};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithOneMember() {
        Character[] items = {'a'};
        Character[] expected = {'a'};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsSortedCollection() {
        Integer[] items = {1, 2, 3, 4, 5, 6};
        Integer[] expected = {1, 2, 3, 4, 5, 6};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionOfCustomObjects() {
        Contrived[] items = {new Contrived(19, 'a'), new Contrived(1, 'a'), new Contrived(3, 'b')};
        Contrived[] expected = {new Contrived(1, 'a'), new Contrived(3, 'b'), new Contrived(19, 'a')};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void emptyCollectionReturnsEmptyCollection() {
        String[] items = {};
        String[] expected = {};

        mergeSort(items);

        assertThat(items, is(expected));
    }

    @Test(expected=NullPointerException.class)
    public void nullValuesThrowIllegalArgumentException() {
        mergeSort(null);
    }
}