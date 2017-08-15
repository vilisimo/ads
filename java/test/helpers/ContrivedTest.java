package helpers;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.not;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.assertTrue;

public class ContrivedTest {

    @Test
    public void sameLettersAndNumbersConsideredEqual() {
        Contrived one = new Contrived(1, 'c');
        Contrived two = new Contrived(1, 'c');

        assertThat(one, is(two));
    }

    @Test
    public void differentLettersNumbersSameSumNotEqual() {
        Contrived one = new Contrived(1, 'c'); // = 100
        Contrived two = new Contrived(3, 'a'); // = 100, too

        assertThat(one, not(two));
    }

    @Test
    public void differentLettersNumbersSameSumReturnZeroWhenCompared() {
        Contrived one = new Contrived(1, 'c');
        Contrived two = new Contrived(3, 'a');

        assertThat(one.compareTo(two), is(0));
    }

    @Test
    public void lowerSumReturnsLessHigherSumReturnsMoreThanZero() {
        Contrived one = new Contrived(1, 'a'); // = 98
        Contrived two = new Contrived(2, 'a'); // = 99

        assertTrue(one.compareTo(two) < 0);
        assertTrue(two.compareTo(one) > 0);
    }

    @Test
    public void returnsCorrectStringRepresentation() {
        String expected = "Contrived[1:a]";
        Contrived contrived = new Contrived(1, 'a');

        assertThat(contrived.toString(), is(expected));
    }
}