package com.vilisimo.ads.helpers;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static com.vilisimo.ads.helpers.Strings.letterAt;
import static com.vilisimo.ads.helpers.Strings.nonBlank;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class StringsTest {

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

    @Test
    public void retrievesLetter() {
        String letter = letterAt("word", 3);

        assertThat(letter, is("d"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptIndexGreaterThanWordLength() {
        letterAt("short", 5);
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptNegativeIndex() {
        letterAt("negative", -1);
    }

    @Test
    public void doesNotAcceptNullWord() {
        expectedException.expect(NullPointerException.class);
        expectedException.expectMessage("Word cannot be null");

        letterAt(null, 1);
    }

    @Test
    public void doesNotAllowNullString() {
        expectedException.expect(NullPointerException.class);
        expectedException.expectMessage("String cannot be null");

        nonBlank(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowEmptyString() {
        nonBlank("");
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAllowEmptyStringWithWhiteSpaces() {
        nonBlank("    ");
    }

    @Test
    public void letsThroughValidString() {
        nonBlank("valid");
    }
}
