package helpers;

import java.lang.reflect.Array;

public final class ArrayMerger {

    private ArrayMerger() {
        throw new AssertionError("The class should not be instantiated");
    }

    @SuppressWarnings("unchecked")
    public static <T> T[] mergeArrays(T[]... arrays) {
        int size = 0;
        for (T[] array : arrays) {
            size += array.length;
        }

        T[] merged = (T[]) Array.newInstance(arrays[0].getClass().getComponentType(), size);

        int startIndex = 0;
        for (T[] array : arrays) {
            System.arraycopy(array, 0, merged, startIndex, array.length);
            startIndex += array.length;
        }

        return merged;
    }
}
