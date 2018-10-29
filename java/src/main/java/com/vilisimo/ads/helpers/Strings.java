package com.vilisimo.ads.helpers;

import static com.vilisimo.ads.helpers.NumberValidator.greaterThan;
import static com.vilisimo.ads.helpers.NumberValidator.lessThan;
import static java.util.Objects.requireNonNull;

public final class Strings {

    private Strings() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static String letterAt(String word, int position) {
        requireNonNull(word, "Word cannot be null");
        greaterThan(-1, position, "Position must be a zero or a positive number");
        lessThan(word.length(), position, "Position cannot be greater than word length (counting from 0)");

        return String.valueOf(word.charAt(position));
    }

    public static void nonBlank(String string) {
        nonBlank(string, "String cannot be null");
    }

    public static void nonBlank(String string, String message) {
        requireNonNull(string, "String cannot be null");

        if (string.trim().isEmpty()) {
            throw new IllegalArgumentException(message);
        }
    }
}
