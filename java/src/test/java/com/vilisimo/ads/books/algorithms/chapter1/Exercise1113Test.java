package com.vilisimo.ads.books.algorithms.chapter1;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

public class Exercise1113Test {

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowEmptyArrays() {
        Exercise1113.transpose(new Integer[0][0], Integer.class);
    }

    @Test
    public void transposesArray() {
        //given
        var array = new Integer[][] { {1, 2, 3}, {9, 8, 7} };

        //when
        var result = Exercise1113.transpose(array, Integer.class);

        //then
        var expected = new Integer[][] { {1, 9}, {2, 8}, {3, 7} };

        assertThat(result, is(expected));
    }
}