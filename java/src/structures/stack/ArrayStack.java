package structures.stack;

import java.util.EmptyStackException;

import static java.util.Objects.requireNonNull;

public class ArrayStack<E> implements Stack<E> {

    private int capacity = 2;
    private E[] elements;
    private int size = 0;

    @SuppressWarnings("unchecked")
    public ArrayStack() {
        this.elements = (E[]) new Object[this.capacity];
    }

    @SuppressWarnings("unchecked")
    public ArrayStack(int initialCapacity) {
        if (initialCapacity < 1) {
            throw new IllegalArgumentException("Initial capacity must be greater than 0");
        }

        this.capacity = initialCapacity;
        this.elements = (E[]) new Object[this.capacity];
    }

    @Override
    public E push(E element) {
        requireNonNull(element, "Null elements cannot be pushed onto a stack");

        if (isFull()) {
            expand();
        }

        elements[size++] = element;

        return element;
    }

    @Override
    public E pop() {
        assertNotEmpty();

        return elements[--size];
    }

    @Override
    public E peek() {
        assertNotEmpty();

        return elements[size - 1];
    }

    @Override
    public boolean isEmpty() {
        return size <= 0;
    }

    @Override
    public int size() {
        return this.size;
    }

    private void assertNotEmpty() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
    }

    private boolean isFull() {
        return size >= elements.length;
    }

    @SuppressWarnings("unchecked")
    private void expand() {
        capacity = capacity * 2;
        E[] temporary = (E[]) new Object[capacity];
        System.arraycopy(this.elements, 0, temporary, 0, elements.length);
        this.elements = temporary;
    }
}
