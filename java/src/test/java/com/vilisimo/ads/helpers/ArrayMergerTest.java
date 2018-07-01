package com.vilisimo.ads.helpers;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class ArrayMergerTest {

    @Test
    public void mergesMultiElementArrays() {
        Integer[] first = {1, 2, 3};
        Integer[] second = {4, 5, 6};
        Integer[] third = {7, 8, 9};
        Integer[] expected = {1, 2, 3, 4, 5, 6, 7, 8, 9};

        Integer[] merged = ArrayMerger.mergeArrays(first, second, third);

        assertThat(merged, is(expected));
    }

    @Test
    public void mergesOneElementArrays() {
        String[] first = {"a"};
        String[] second = {"b"};
        String[] third = {"c"};
        String[] expected = {"a", "b", "c"};

        String[] merged = ArrayMerger.mergeArrays(first, second, third);

        assertThat(merged, is(expected));
    }

    @Test
    public void mergesEmptyArrays() {
        Contrived[] first = {};
        Contrived[] second = {};
        Contrived[] third = {};

        Contrived[] merged = ArrayMerger.mergeArrays(first, second, third);

        assertThat(merged.length, is(0));
    }
}