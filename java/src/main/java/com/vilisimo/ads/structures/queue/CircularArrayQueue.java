package com.vilisimo.ads.structures.queue;

import java.util.NoSuchElementException;

import static java.util.Objects.requireNonNull;

public class CircularArrayQueue<E> implements Queue<E> {

    private E[] elements;
    private int size = 0;
    private int head = 0;
    private int tail = 0;

    @SuppressWarnings("unchecked")
    public CircularArrayQueue() {
        this.elements = (E[]) new Object[2];
    }

    @SuppressWarnings("unchecked")
    public CircularArrayQueue(int initialCapacity) {
        if (initialCapacity < 1) {
            throw new IllegalArgumentException("Initial capacity must be at least 1");
        }
        this.elements = (E[]) new Object[initialCapacity];
    }

    @Override
    public E enqueue(E element) {
        requireNonNull(element, "Element cannot be null");
        assertNotFull();

        elements[tail++] = element;
        if (tail >= elements.length) {
            tail = 0;
        }
        size++;

        return element;
    }

    @Override
    public E dequeue() {
        assertNotEmpty();

        E element = elements[head++];
        if (head >= elements.length) {
            head = 0;
        }
        size--;

        return element;
    }

    @Override
    public E peek() {
        assertNotEmpty();

        return elements[head];
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size <= 0;
    }

    private boolean isFull() {
        return size >= elements.length;
    }

    private void assertNotFull() {
        if (isFull()) {
            throw new IllegalStateException("The queue is full");
        }
    }

    private void assertNotEmpty() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
    }
}