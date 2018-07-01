package com.vilisimo.ads.structures.stack;

import org.junit.Before;
import org.junit.Test;

import java.util.EmptyStackException;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

public class LinkedStackTest {

    private Stack<Integer> stack;

    @Before
    public void setUp() {
        this.stack = new LinkedStack<>();
    }

    @Test
    public void canPushItemsOnTheStack() {
        Integer pushed = stack.push(1);

        assertThat(pushed, is(1));
    }

    @Test
    public void canPopItemsFromTheStack() {
        Integer pushed = stack.push(1);

        Integer popped = stack.pop();

        assertThat(popped, is(pushed));
    }

    @Test(expected = EmptyStackException.class)
    public void cannotPopEmptyStack() {
        stack.pop();
    }

    @Test
    public void peekingReturnsLastElement() {
        stack.push(1);
        stack.push(2);

        Integer last = stack.peek();

        assertThat(last, is(2));
    }

    @Test
    public void peekingDoesNotRemoveElement() {
        stack.push(1);

        stack.peek();

        assertFalse(stack.isEmpty());
    }

    @Test
    public void emptyStackHasZeroSize() {
        assertThat(stack.size(), is(0));
    }

    @Test
    public void pushingElementIncreasesStackSize() {
        stack.push(1);

        assertThat(stack.size(), is(1));
    }

    @Test(expected = NullPointerException.class)
    public void cannotPushNullValues() {
        stack.push(null);
    }

    @Test
    public void poppingElementDecreasesStackSize() {
        stack.push(1);
        assertThat(stack.size(), is(1));

        stack.pop();
        assertThat(stack.size(), is(0));
    }

    @Test
    public void emptyStackIsEmpty() {
        assertTrue(stack.isEmpty());
    }

    @Test
    public void nonEmptyStackIsNotEmpty() {
        stack.push(1);

        assertFalse(stack.isEmpty());
    }
}