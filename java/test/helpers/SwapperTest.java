package helpers;

import org.junit.Test;

import static helpers.Swapper.swap;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class SwapperTest {

    @Test
    public void swapsElements() {
        String[] letters = {"a", "b", "c"};
        String[] expected = {"c", "b", "a"};

        swap(letters, 0, 2);

        assertThat(letters, is(expected));
    }

    @Test
    public void samePositionsSameArray() {
        Integer[] numbers = {1, 2, 3};
        Integer[] expected = {3, 2, 1};

        swap(numbers, 0, 2);

        assertThat(numbers, is(expected));
    }

    @Test(expected = IllegalArgumentException.class)
    public void doesNotAcceptNull() {
        swap(null, 0, 1);
    }
}