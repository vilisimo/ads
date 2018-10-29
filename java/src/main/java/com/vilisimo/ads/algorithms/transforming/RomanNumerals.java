package com.vilisimo.ads.algorithms.transforming;

import com.vilisimo.ads.helpers.NumberValidator;
import com.vilisimo.ads.helpers.Strings;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

import static com.vilisimo.ads.helpers.Strings.nonBlank;

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

    public static int toLatin(String roman) {
        nonBlank(roman, "String must be a valid Roman numeral");

        var numerals = compactNumerals();
        int total = 0;

        for (int i = 0; i < roman.length(); i++) {
            var firstNumeral = Strings.letterAt(roman, i);
            var firstLatin = numerals.get(firstNumeral);
            checkNumeral(firstLatin, firstNumeral);

            if (i + 1 < roman.length()) {
                var secondNumeral = Strings.letterAt(roman, i + 1);
                var secondLatin = numerals.get(secondNumeral);
                checkNumeral(secondLatin, secondNumeral);

                if (firstLatin < secondLatin) {
                    total -= firstLatin;
                } else {
                    total += firstLatin;
                }

            } else {
                total += firstLatin;
            }
        }

        if (!roman.equals(toRoman(total))) {
            throw new IllegalArgumentException(roman + " is not a valid Roman numeral");
        }

        return total;
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

    private static Map<String, Integer> compactNumerals() {
        var numerals = new LinkedHashMap<String, Integer>(7);

        numerals.put("I", 1);
        numerals.put("V", 5);
        numerals.put("X", 10);
        numerals.put("L", 50);
        numerals.put("C", 100);
        numerals.put("D", 500);
        numerals.put("M", 1000);

        return numerals;
    }

    private static void checkNumeral(Integer value, String letter) {
        if (value == null) {
            throw new IllegalArgumentException("[" + letter + "] is not a valid Roman numeral");
        }
    }
}
