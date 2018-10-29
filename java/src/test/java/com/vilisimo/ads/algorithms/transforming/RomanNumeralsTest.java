package com.vilisimo.ads.algorithms.transforming;

import org.junit.Test;

import static com.vilisimo.ads.algorithms.transforming.RomanNumerals.toLatin;
import static com.vilisimo.ads.algorithms.transforming.RomanNumerals.toRoman;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class RomanNumeralsTest {

    @Test
    public void convertsNumberToRoman() {
        var min = toRoman(1);
        var max = toRoman(3999);

        assertThat(min, is("I"));
        assertThat(max, is("MMMCMXCIX"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowGreaterThan3999() {
        toRoman(4000);
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowLessThan1() {
        toRoman(0);
    }

    @Test
    public void convertsRomanToLatin() {
        int roman = toLatin("I");
    }
}
