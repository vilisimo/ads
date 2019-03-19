package com.vilisimo.ads.books.algorithms.chapter1;

import com.vilisimo.ads.helpers.NumberValidator;

public class Exercise1114 {

    /**
     * Calculates base 2 logarithm.
     * @param n a number for which to calculate base 2 logarithm
     * @return
     */
    public static int lg(int n) {
        NumberValidator.greaterThan(0, n);

        var answer = 0;
        while (n > 0) {
            n /= 2;
            answer++;
        }

        return answer - 1;
    }
}
