package structures.stack;

import java.util.EmptyStackException;
import java.util.LinkedList;

import static java.util.Objects.requireNonNull;

public class LinkedStack<E> implements Stack<E> {

    private LinkedList<E> list = new LinkedList<>();
    private int size = 0;

    @Override
    public E push(E element) {
        requireNonNull(element, "Null elements cannot be pushed onto a stack");

        list.push(element);
        size++;

        return element;
    }

    @Override
    public E pop() {
        assertNotEmpty();
        size--;

        return list.pop();
    }

    @Override
    public E peek() {
        assertNotEmpty();

        return list.peek();
    }

    @Override
    public boolean isEmpty() {
        return size <= 0;
    }

    @Override
    public int size() {
        return size;
    }

    private void assertNotEmpty() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
    }
}
