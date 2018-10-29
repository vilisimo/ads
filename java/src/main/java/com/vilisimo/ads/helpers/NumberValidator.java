package com.vilisimo.ads.helpers;

public final class NumberValidator {

    private NumberValidator() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static void lessThan(int lessThan, int number) {
        lessThan(lessThan, number, number + " cannot be greater than " + lessThan);
    }

    public static void lessThan(int lessThan, int number, String message) {
        if (number >= lessThan) {
            throw new IllegalArgumentException(message);
        }
    }

    public static void greaterThan(int greaterThan, int number) {
        greaterThan(greaterThan, number, number + " cannot be less than " + greaterThan);
        if (number <= greaterThan) {
            throw new IllegalArgumentException(number + " cannot be less than " + greaterThan);
        }
    }

    public static void greaterThan(int greaterThan, int number, String message) {
        if (number <= greaterThan) {
            throw new IllegalArgumentException(message);
        }
    }
}
