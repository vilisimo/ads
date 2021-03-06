package com.vilisimo.ads.algorithms.sorting;

import com.vilisimo.ads.helpers.Contrived;
import org.junit.Test;

import static com.vilisimo.ads.algorithms.sorting.QuickSortInPlace.quicksort;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class QuickSortInPlaceTest {

    @Test
    public void sortsCollection() {
        String[] items = {"d", "z", "a"};
        String[] expected = {"a", "d", "z"};

        quicksort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsPartiallySortedCollection() {
        Integer[] items = {1, 1, -3, 1, 13, 9};
        Integer[] expected = {-3, 1, 1, 1, 9, 13};

        quicksort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsCollectionWithOneMember() {
        Character[] items = {'a'};
        Character[] expected = {'a'};

        quicksort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void sortsSortedCollection() {
        String[] items = {"a", "b", "c", "d", "e", "f"};
        String[] expected = {"a", "b", "c", "d", "e", "f"};

        quicksort(items);

        assertThat(items, is(expected));
    }

    @Test
    public void emptyCollectionReturnsEmptyCollection() {
        String[] items = {};
        String[] expected = {};

        quicksort(items);

        assertThat(items, is(expected));
    }

    @Test(expected=NullPointerException.class)
    public void nullValuesThrowIllegalArgumentException() {
        quicksort(null);
    }

    @Test
    public void sortsCollectionOfCustomObjects() {
        Contrived[] items = {new Contrived(19, 'a'), new Contrived(1, 'a'), new Contrived(3, 'b')};
        Contrived[] expected = {new Contrived(1, 'a'), new Contrived(3, 'b'), new Contrived(19, 'a')};

        quicksort(items);

        assertThat(items, is(expected));
    }
}