package com.vilisimo.ads.books.algorithms.chapter1;

import com.vilisimo.ads.helpers.ArrayValidator;

import java.lang.reflect.Array;

public class Exercise1113 {

    /**
     * Transposes the array.
     *
     * @param array array to be transposed
     * @param <A> element in an array
     * @return transposed array
     */
    @SuppressWarnings("unchecked")
    public static <A> A[][] transpose(A[][] array, Class<? extends A> type) {
        ArrayValidator.TwoD.nonEmpty(array);

        var newColumns = array.length; // returns row count, but due to transposition it becomes column count
        var newRows = array[0].length; // returns column count, but due to transposition it becomes row count
        var newArray = (A[][]) Array.newInstance(type, newRows, newColumns);

        for (int row = 0; row < newRows; row++) {
            for (int column = 0; column < newColumns; column++) {
                newArray[row][column] = array[column][row];
            }
        }

        return newArray;
    }
}
