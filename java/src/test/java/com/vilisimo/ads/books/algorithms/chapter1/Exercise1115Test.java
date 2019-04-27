package com.vilisimo.ads.books.algorithms.chapter1;

import org.junit.Test;

import java.util.Arrays;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class Exercise1115Test {

    @Test
    public void calculatesFrequencies() {
        //given
        int[] input = {1, 2, 2, 3, 4, 5, 2, 2};

        //when
        int[] result = Exercise1115.histogram(input, 6);

        //then
        assertThat(result, is(new int[] {0, 1, 4, 1, 1, 1}));
    }

    @Test
    public void doesNotCalculateFrequenciesForNumbersOutsideRange() {
        //given
        int[] input = {1, 2, 3, 3};

        //when
        int[] result = Exercise1115.histogram(input, 3);

        //then
        assertThat(result.length, is(3));
        assertThat(result[2], is(1));
    }

    @Test
    public void frequenciesAddUpToEntriesCount() {
        //given
        int[] input = {0, 0, 1, 2, 2};

        //when
        int[] result = Exercise1115.histogram(input, 3);

        //then
        int sum = Arrays.stream(result)
                .sum();

        assertThat(sum, is(input.length));
    }
}
