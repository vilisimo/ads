package com.vilisimo.ads.helpers;

import org.junit.Test;

import static com.vilisimo.ads.helpers.NumberValidator.*;

public class NumberValidatorTest {

    @Test(expected = IllegalArgumentException.class)
    public void recognizesTooLargeNumbers() {
        lessThan(1, 1);
    }

    @Test
    public void letsThroughSmallerNumbers() {
        lessThan(1, 0);
    }

    @Test(expected = IllegalArgumentException.class)
    public void recognizesTooSmallNumbers() {
        greaterThan(0, 0);
    }

    @Test
    public void letsThroughLargerNumbers() {
        greaterThan(0, 1);
    }
}