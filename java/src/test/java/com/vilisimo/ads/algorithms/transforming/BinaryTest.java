package com.vilisimo.ads.algorithms.transforming;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

public class BinaryTest {

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptNegativeNumbers() {
        Binary.toBinaryString(-1);
    }

    @Test
    public void transformsToBinaryRepresentation() {
        //when
        var zero = Binary.toBinaryString(0);
        var one = Binary.toBinaryString(1);
        var two = Binary.toBinaryString(2);
        var three = Binary.toBinaryString(3);
        var ten = Binary.toBinaryString(10);


        //then
        assertThat(zero, is("0"));
        assertThat(one, is("1"));
        assertThat(two, is("10"));
        assertThat(three, is("11"));
        assertThat(ten, is("1010"));
    }
}