package algorithms.sorting;

import org.junit.Test;

import static algorithms.sorting.QuickSort.sort;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class QuickSortTest {

    @Test
    public void sortsCollection() {
        String[] items = {"d", "z", "a"};
        String[] expected = {"a", "d", "z"};

        items = sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithOneMember() {
        String[] items = {"a"};
        String[] expected = {"a"};

        items = sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsSortedCollection() {
        String[] items = {"a", "b", "c", "d", "e", "f"};
        String[] expected = {"a", "b", "c", "d", "e", "f"};

        items = sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void emptyCollectionReturnsEmptyCollection() {
        String[] items = {};
        String[] expected = {};

        items = sort(items);

        assertThat(items, is(expected));
    }

    @Test(expected=NullPointerException.class)
    public void nullValuesThrowIllegalArgumentException() {
        sort(null);
    }
}