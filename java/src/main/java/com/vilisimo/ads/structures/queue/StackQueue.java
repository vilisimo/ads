package com.vilisimo.ads.structures.queue;

import java.util.NoSuchElementException;
import java.util.Stack;

import static java.util.Objects.requireNonNull;

/**
 * Not the most efficient implementation of a queue,
 * but interesting one nevertheless.
 */
public class StackQueue<E> implements Queue<E> {

    private Stack<E> incoming = new Stack<>();
    private Stack<E> outgoing = new Stack<>();
    private int size = 0;

    @Override
    public E enqueue(E element) {
        requireNonNull(element, "Element cannot be null");

        incoming.push(element);
        size++;

        return element;
    }

    @Override
    public E dequeue() {
        assertNotEmpty();
        transferElementsIfNeeded();
        size--;

        return outgoing.pop();
    }

    @Override
    public E peek() {
        assertNotEmpty();
        transferElementsIfNeeded();

        return outgoing.peek();
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size <= 0;
    }

    private void assertNotEmpty() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
    }

    private void transferElementsIfNeeded() {
        if (outgoing.isEmpty()) {
            while (!incoming.isEmpty()) {
                outgoing.push(incoming.pop());
            }
        }
    }
}
