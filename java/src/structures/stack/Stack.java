package structures.stack;

public interface Stack<E> {
    E push(E element);
    E pop();
    E peek();
    boolean isEmpty();
    int size();
}
