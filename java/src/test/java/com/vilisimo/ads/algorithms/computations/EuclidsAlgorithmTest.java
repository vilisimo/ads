package com.vilisimo.ads.algorithms.computations;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class EuclidsAlgorithmTest {

    @Test
    public void calculatesGcdWhenItExists() {
        var result = EuclidsAlgorithm.calculateGcd(100, 60);
        var result2 = EuclidsAlgorithm.calculateGcd(450, 70);

        assertThat(result, is(20));
        assertThat(result2, is(10));
    }

    @Test
    public void whenFirstArgumentIsSmallerThanSecondCalculatesGcd() {
        var result = EuclidsAlgorithm.calculateGcd(60, 100);

        assertThat(result, is(20));
    }

    @Test
    public void whenArgumentsAreZeroReturnsGcdMatchingNonZeroArgument() {
        var first = EuclidsAlgorithm.calculateGcd(0, 100);
        var second = EuclidsAlgorithm.calculateGcd(100, 0);

        assertThat(first, is(100));
        assertThat(second, is(100));
    }
}
