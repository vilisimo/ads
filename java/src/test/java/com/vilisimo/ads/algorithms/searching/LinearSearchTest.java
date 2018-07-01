package com.vilisimo.ads.algorithms.searching;

import com.vilisimo.ads.helpers.Contrived;
import org.junit.Test;

import static com.vilisimo.ads.algorithms.searching.LinearSearch.search;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class LinearSearchTest {

    @Test(expected=NullPointerException.class)
    public void nullCollectionThrowsException() {
        search(null, 1);
    }

    @Test(expected=NullPointerException.class)
    public void nullTargetThrowsException() {
        search(new Integer[] {1}, null);
    }

    @Test
    public void emptyCollectionReturnsMinusOne() {
        search(new Integer[] {}, 1);
    }

    @Test
    public void searchingForNonExistentElementReturnsMinusOne() {
        int actual = search(new Integer[] {1, 2, 3}, 99);

        assertThat(actual, is(-1));
    }

    @Test
    public void searchForElementReturnsCorrectPosition() {
        int actual = search(new Integer[] {3, 123, 3223}, 123);

        assertThat(actual, is(1));
    }

    @Test
    public void searchForLowBoundaryElementReturnsCorrectPosition() {
        int actual = search(new Integer[] {1, 2, 3}, 1);

        assertThat(actual, is(0));
    }

    @Test
    public void searchForHighBoundaryElementReturnsCorrectPosition() {
        int actual = search(new Integer[] {1, 2, 3}, 3);

        assertThat(actual, is(2));
    }

    @Test
    public void repeatingNumbersReturnFirstOccurrence() {
        int actual = search(new Integer[] {1, 2, 2, 3}, 2);

        assertThat(actual, is(1));
    }

    @Test
    public void searchCustomObjects() {
        Contrived[] array = {
                new Contrived(122, 'a'),
                new Contrived(13, 'b'),
                new Contrived(3321, 'f')
        };

        int actual = search(array, new Contrived(13, 'b'));

        assertThat(actual, is(1));
    }

    @Test
    public void searchUnsortedArrayFindsCorrectPosition() {
        int actual = search(new Integer[] {2, 13, 4, 1, 33}, 4);

        assertThat(actual, is(2));
    }
}