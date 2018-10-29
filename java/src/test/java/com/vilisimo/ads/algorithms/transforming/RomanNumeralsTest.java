package com.vilisimo.ads.algorithms.transforming;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static com.vilisimo.ads.algorithms.transforming.RomanNumerals.toLatin;
import static com.vilisimo.ads.algorithms.transforming.RomanNumerals.toRoman;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class RomanNumeralsTest {

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

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
        var min = toLatin("I");
        var max = toLatin("MMMCMXCIX");

        assertThat(min, is(1));
        assertThat(max, is(3999));
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowUnfitStrings() {
        toLatin("Unfit");
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowEmptyStrings() {
        toLatin("");
    }

    @Test
    public void doesNotAllowNullString() {
        expectedException.expect(NullPointerException.class);
        expectedException.expectMessage("String cannot be null");

        toLatin(null);
    }

    @Test
    public void doesNotAllowSneakyPseudoRomanNumerals() {
        expectedException.expect(IllegalArgumentException.class);
        expectedException.expectMessage("[F] is not a valid Roman numeral");

        toLatin("XXFX");
    }
}
