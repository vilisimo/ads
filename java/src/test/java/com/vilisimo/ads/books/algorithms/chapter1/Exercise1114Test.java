package com.vilisimo.ads.books.algorithms.chapter1;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

public class Exercise1114Test {

    @Test
    public void computesLogarithmOnNonZeroNumbers() {
        //when
        var lg1 = Exercise1114.lg(1);
        var lg10 = Exercise1114.lg(10);
        var lg100 = Exercise1114.lg(100);

        //then
        assertThat(lg1, is(0));
        assertThat(lg10, is(3));
        assertThat(lg100, is(6));
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptNegativeNumbers() {
        Exercise1114.lg(-1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptZero() {
        Exercise1114.lg(0);
    }
}