package algorithms.sorting;

import helpers.Contrived;
import org.junit.Test;

import static algorithms.sorting.SelectionSort.sort;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class SelectionSortTest {

    @Test
    public void sortsCollection() {
        String[] items = {"d", "z", "a"};
        String[] expected = {"a", "d", "z"};

        sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithEdgeCases() {
        Integer[] items = {1, 1, -3, 1, 13, 9};
        Integer[] expected = {-3, 1, 1, 1, 9, 13};

        sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithOneMember() {
        Character[] items = {'a'};
        Character[] expected = {'a'};

        sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionOfCustomObjects() {
        Contrived[] items = {new Contrived(19, 'a'), new Contrived(1, 'a'), new Contrived(3, 'b')};
        Contrived[] expected = {new Contrived(1, 'a'), new Contrived(3, 'b'), new Contrived(19, 'a')};

        sort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void emptyCollectionReturnsEmptyCollection() {
        String[] items = {};
        String[] expected = {};

        sort(items);

        assertThat(items, is(expected));
    }

    @Test(expected=IllegalArgumentException.class)
    public void nullValuesThrowIllegalArgumentException() {
        sort(null);
    }
}
