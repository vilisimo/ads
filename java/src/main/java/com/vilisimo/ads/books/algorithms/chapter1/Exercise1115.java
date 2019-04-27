package com.vilisimo.ads.books.algorithms.chapter1;

public class Exercise1115 {

    public static int[] histogram(int[] input, int size) {
        int[] result = new int[size];

        for (int number : input) {
            if (size - 1 >= number) {
                result[number]++;
            }
        }

        return result;
    }
}
