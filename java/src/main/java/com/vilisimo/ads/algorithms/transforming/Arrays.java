package com.vilisimo.ads.algorithms.transforming;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Arrays {

    private static final String TRUE = "*";
    private static final String FALSE = " ";

    private Arrays() {
        throw new AssertionError("The class should not be instantiated");
    }

    /**
     * Transforms contents of two dimensional boolean array into a table,
     * where "*" represents true and " " (empty space) represents false.
     *
     * @param input 2D array to be represented as table
     * @return a String representation of 2D array
     */
    public static String toTable(boolean[][] input) {
        if (input.length == 0 || input[0].length == 0) {
            return "";
        }

        var width = input[0].length;
        var height = input.length;

        var header = " " + IntStream.range(0, width)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining());

        var rows = "";
        for (var h = 0; h < height; h++) {
            var row = "" + h;
            for (var w = 0; w < width; w++) {
                row += input[h][w] ? TRUE : FALSE;
            }
            rows += "\n" + row;
        }

        return header + rows;
    }
}
