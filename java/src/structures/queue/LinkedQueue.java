package structures.queue;

import java.util.LinkedList;
import java.util.NoSuchElementException;

import static java.util.Objects.requireNonNull;

public class LinkedQueue<E> implements Queue<E> {

    private LinkedList<E> elements = new LinkedList<>();
    private int size = 0;

    @Override
    public E enqueue(E element) {
        requireNonNull(element);

        elements.addLast(element);
        size++;

        return element;
    }

    @Override
    public E dequeue() {
        assertNotEmpty();

        size--;

        return elements.pop();
    }

    @Override
    public E peek() {
        assertNotEmpty();

        return elements.peek();
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
}
