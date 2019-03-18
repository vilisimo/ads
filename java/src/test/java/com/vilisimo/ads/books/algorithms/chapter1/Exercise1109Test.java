package com.vilisimo.ads.books.algorithms.chapter1;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class Exercise1109Test {

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptNegativeNumbers() {
        Exercise1109.toBinaryString(-1);
    }

    @Test
    public void transformsToBinaryRepresentation() {
        //when
        var zero = Exercise1109.toBinaryString(0);
        var one = Exercise1109.toBinaryString(1);
        var two = Exercise1109.toBinaryString(2);
        var three = Exercise1109.toBinaryString(3);
        var ten = Exercise1109.toBinaryString(10);


        //then
        assertThat(zero, is("0"));
        assertThat(one, is("1"));
        assertThat(two, is("10"));
        assertThat(three, is("11"));
        assertThat(ten, is("1010"));
    }
}