package com.vilisimo.ads.helpers;

import org.junit.Test;

import static com.vilisimo.ads.helpers.Comparer.equal;
import static com.vilisimo.ads.helpers.Comparer.greater;
import static com.vilisimo.ads.helpers.Comparer.less;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class ComparerTest {

    @Test
    public void bIsGreaterThanA() {
        assertTrue(greater("b", "a"));
    }

    @Test
    public void aIsNotGreaterThanB() {
        assertFalse(greater("a", "b"));
    }

    @Test
    public void aIsNotGreaterThanA() {
        assertFalse(greater("a", "a"));
    }

    @Test
    public void aIsEqualA() {
        assertTrue(equal("a", "a"));
    }

    @Test
    public void aIsNotEqualB() {
        assertFalse(equal("a", "b"));
    }

    @Test
    public void aIsLessThanB() {
        assertTrue(less("a", "b"));
    }

    @Test
    public void bIsNotLessThanA() {
        assertFalse(less("b", "a"));
    }

    @Test
    public void bIsNotLessThanB() {
        assertFalse(less("b", "b"));
    }
}