package com.vilisimo.ads.algorithms.transforming;

import com.vilisimo.ads.helpers.NumberValidator;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

public class RomanNumerals {

    private static Map<Integer, String> numerals = numerals();

    private static int UPPER_BOUNDARY = 4000;
    private static int LOWER_BOUNDARY = 0;


    public static String toRoman(int latin) {
        NumberValidator.lessThan(UPPER_BOUNDARY, latin);
        NumberValidator.greaterThan(LOWER_BOUNDARY, latin);

        var letters = new ArrayList<String>();

        for (var numeral : numerals.entrySet()) {

            String letter = numeral.getValue();
            Integer letterValue = numeral.getKey();

            while (latin >= letterValue) {
                latin -= letterValue;
                letters.add(letter);
            }
        }

        return String.join("", letters);
    }

    private static Map<Integer, String> numerals() {
        var numerals = new LinkedHashMap<Integer, String>(13);

        numerals.put(1000, "M");
        numerals.put(900, "CM");
        numerals.put(500, "D");
        numerals.put(400, "CD");
        numerals.put(100, "C");
        numerals.put(90, "XC");
        numerals.put(50, "L");
        numerals.put(40, "XL");
        numerals.put(10, "X");
        numerals.put(9, "IX");
        numerals.put(5, "V");
        numerals.put(4, "IV");
        numerals.put(1, "I");

        return numerals;
    }
}