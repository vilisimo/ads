package com.vilisimo.ads.helpers;

public final class NumberValidator {

    private NumberValidator() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static void lessThan(int lessThan, int number) {
        if (number >= lessThan) {
            throw new IllegalArgumentException(number + " cannot be greater than " + lessThan);
        }
    }

    public static void greaterThan(int greaterThan, int number) {
        if (number <= greaterThan) {
            throw new IllegalArgumentException(number + " cannot be less than " + greaterThan);
        }
    }
}
