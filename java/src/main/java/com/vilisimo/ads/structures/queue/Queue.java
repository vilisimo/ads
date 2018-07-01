package com.vilisimo.ads.structures.queue;

public interface Queue<E> {
    E enqueue(E element);
    E dequeue();
    E peek();
    int size();
    boolean isEmpty();
}
