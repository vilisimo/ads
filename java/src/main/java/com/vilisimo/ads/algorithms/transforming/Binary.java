package com.vilisimo.ads.algorithms.transforming;

import com.vilisimo.ads.helpers.NumberValidator;

public final class Binary {

    private Binary() {
        throw new AssertionError("The class should not be instantiated");
    }

    /**
     * Similar as {@link Integer#toBinaryString}, but not as robust.
     * Also, does not work with negative numbers to make the implementation
     * easier.
     *
     * @param n integer to convert to a binary string
     * @return a binary string representation of n
     */
    public static String toBinaryString(int n) {
        NumberValidator.greaterThan(-1, n);

        if (n == 0) {
            return "0";
        }

        String result = "";
        for (var i = n; i > 0; i /= 2) {
            result = (i % 2) + result;
        }

        return result;
    }
}
