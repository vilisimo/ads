package com.vilisimo.ads.helpers;

public class ArrayValidator {
    public static class TwoD {
        public static <A> void nonEmpty(A[][] array) {
            if (array == null) {
                throw new NullPointerException("Array cannot be null");
            }

            if (array.length == 0 || array[0].length == 0) {
                throw new IllegalArgumentException("Array or its contents cannot be empty");
            }
        }
    }
}
