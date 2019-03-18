package com.vilisimo.ads.helpers;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

public class ArrayValidatorTest {

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

    @Test
    public void allowsNonEmptyArray() {
        //given
        var array = new Integer[1][1];
        array[0][0] = 1;

        //when
        ArrayValidator.TwoD.nonEmpty(array);
    }

    @Test
    public void doesNotAllowNullArrays() {
        //given
        expectedException.expect(NullPointerException.class);
        expectedException.expectMessage("cannot be null");

        //when
        ArrayValidator.TwoD.nonEmpty(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowEmptyArrays() {
        ArrayValidator.TwoD.nonEmpty(new Integer[0][0]);
    }
}