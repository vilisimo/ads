package com.vilisimo.ads.structures.queue;

import org.junit.Before;
import org.junit.Test;

import java.util.NoSuchElementException;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

public class CircularArrayQueueTest {

    private Queue<String> queue;

    @Before
    public void setUp() {
        queue = new CircularArrayQueue<>(2);
    }

    @Test(expected = IllegalArgumentException.class)
    public void capacityOfOneOrMoreIsEnforced() {
        queue = new CircularArrayQueue<>(0);
    }

    @Test
    public void enqueueAddsElement() {
        queue.enqueue("Placeholder");

        String result = queue.dequeue();

        assertThat(result, is("Placeholder"));
    }

    @Test(expected = IllegalStateException.class)
    public void enqueueEnforcesMaxCapacity() {
        queue.enqueue("a");
        queue.enqueue("b");
        queue.enqueue("c");
    }

    @Test(expected = NullPointerException.class)
    public void enqueueDoesNotAllowNulls() {
        queue.enqueue(null);
    }

    @Test
    public void dequeueReturnsFirstElement() {
        queue.enqueue("Placeholder");
        queue.enqueue("Another");

        String result = queue.dequeue();

        assertThat(result, is("Placeholder"));
    }

    @Test(expected = NoSuchElementException.class)
    public void dequeuingEmptyQueueThrowsException() {
        queue.dequeue();
    }

    @Test
    public void tailWraps() {
        queue.enqueue("a"); // head = 0, tail = 1
        queue.enqueue("b"); // head = 0, tail = 0
        queue.dequeue();            // head = 1, tail = 0
        queue.enqueue("c"); // head = 1, tail = 1
        queue.dequeue();            // head = 0, tail = 1

        String result = queue.dequeue();

        assertThat(result, is("c"));
    }

    @Test
    public void headWraps() {
        queue.enqueue("a"); // head = 0, tail = 1
        queue.enqueue("b"); // head = 0, tail = 0
        queue.dequeue();            // head = 1, tail = 0
        queue.dequeue();            // head = 0, tail = 0
        queue.enqueue("c"); // head = 0, tail = 1

        String result = queue.dequeue();

        assertThat(result, is("c"));
    }

    @Test
    public void peekReturnsLastElement() {
        queue.enqueue("Placeholder");

        assertThat(queue.peek(), is("Placeholder"));
    }

    @Test(expected = NoSuchElementException.class)
    public void peekOnEmptyQueueThrowsException() {
        queue.peek();
    }

    @Test
    public void emptyQueueHasSizeZero() {
        assertThat(queue.size(), is(0));
    }

    @Test
    public void addingElementIncrementsSize() {
        int initial = queue.size();

        queue.enqueue("Placeholder");

        assertThat(initial, is(queue.size() - 1));
    }

    @Test
    public void dequeuingElementDecrementsSize() {
        queue.enqueue("Placeholder");
        int initial = queue.size();

        queue.dequeue();

        assertThat(initial, is(queue.size() + 1));
    }

    @Test
    public void emptyQueueIsEmpty() {
        assertTrue(queue.isEmpty());
    }
}