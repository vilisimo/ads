package com.vilisimo.ads.helpers;

public final class Comparer {

    private Comparer() {
        throw new AssertionError("The class should not be instantiated");
    }

    public static <E extends Comparable<E>> boolean greater(E first, E second) {
        return first.compareTo(second) > 0;
    }

    public static <E extends Comparable<E>> boolean equal(E first, E second) {
        return first.compareTo(second) == 0;
    }

    public static <E extends Comparable<E>> boolean less(E first, E second) {
        return first.compareTo(second) < 0;
    }
}
